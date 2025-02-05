import os
from openai import OpenAI
from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup
from seleniumwire import webdriver  # Use selenium-wire instead of regular selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import requests
import re

# Initialize the OpenAI client

app = Flask(__name__)

# Replace this with your actual Slack webhook URL
WEBHOOK_URL = "https://hooks.slack.com/triggers/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"
def format_subtitles(subtitles, chunk_size=72):
    """
    Formats subtitles into larger chunks, each containing multiple lines of dialogue with a broader timestamp range.
    Returns the formatted subtitles as a single string.
    """
    lines = subtitles.split('\n')
    dialogue_lines = []
    timestamps = []

    timestamp_pattern = re.compile(r'^\d{2}:\d{2}:\d{2}[.,]\d{3} --> \d{2}:\d{2}:\d{2}[.,]\d{3}$')
    line_number_pattern = re.compile(r'^\d+$')

    start_time = ""
    end_time = ""
    formatted_subtitles = []

    for line in lines:
        if line_number_pattern.match(line):
            continue

        if timestamp_pattern.match(line):
            current_start, current_end = line.split(' --> ')
            if not start_time:
                start_time = current_start
            end_time = current_end
            timestamps.append((current_start, current_end))
            continue

        if not line.strip():
            continue

        dialogue_lines.append(line.strip())

    for i in range(0, len(dialogue_lines), chunk_size):
        current_chunk = dialogue_lines[i:i + chunk_size]
        if current_chunk:
            chunk_start_time = timestamps[i][0] if i < len(timestamps) else "00:00:00,000"
            chunk_end_time = timestamps[min(i + chunk_size - 1, len(timestamps) - 1)][1] if i + chunk_size - 1 < len(timestamps) else end_time
            formatted_chunk = f"{chunk_start_time} --> {chunk_end_time}\n{' '.join(current_chunk)}"
            formatted_subtitles.append(formatted_chunk)

    return "\n\n".join(formatted_subtitles)

def perform_key_sequence(driver):
    actions = webdriver.ActionChains(driver)
    actions.send_keys("c")
    actions.pause(0.1)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.pause(0.1)
    actions.send_keys(Keys.RETURN)
    actions.perform()

def find_and_click_play_button(driver,url):
    """
    Finds and clicks the play button within the iframe.
    """
    driver.get(url)
    time.sleep(5)  # Adjust if needed

    iframe = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//iframe[contains(@src, 'vimeo.com')]"))
    )
    driver.switch_to.frame(iframe)

    play_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@data-play-button='true']"))
    )
    play_button.click()

    perform_key_sequence()

def monitor_network_for_vtt(driver):
    """
    Monitors network traffic for .vtt files using selenium-wire and returns their text content.
    """
    start_time = time.time()
    timeout = 15  # Poll for 15 seconds before reloading

    while time.time() - start_time < timeout:
        for request in driver.requests:
            if request.response and ".vtt" in request.url:
                try:
                    response = requests.get(request.url)
                    response.raise_for_status()
                    return response.text
                except requests.RequestException:
                    pass
        time.sleep(1)

    driver.refresh()
    time.sleep(5)
    find_and_click_play_button()

def fetch_transcript(url):
    try:
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_experimental_option("detach", True)  # Keep browser open after script finishes

    # Initialize the WebDriver with selenium-wire
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        find_and_click_play_button(driver,url)
        subtitles_text = monitor_network_for_vtt(driver)
        formatted_subtitles = format_subtitles(subtitles_text[7:])
        return(formatted_subtitles)

    except Exception as e:
        formatted_subtitles = f"An error occurred: {e}"
    
    driver.close()

@app.route('/send-url', methods=['POST'])
def send_url():
    # Retrieve the URL from the JSON payload
    data = request.json
    url = data.get("url")

    # Parse the webpage content
    text_content = fetch_transcript(url)

    # Limit the text to avoid excessive token usage (e.g., 2000 characters)
    #text_content = text_content[:2000]

    # Use OpenAI's chat model to summarize the text
    try:
        client = OpenAI(
            # api_key=os.getenv("OPENAI_API_KEY")
            api_key=("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")
        )

        completion = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You're an assistant summarizing a transcript of a local government meeting for journalists who couldn't attend but need to understand the key events and discussions. Your goal is to provide a detailed, informative summary that captures the essence of the meeting, including specific data points, arguments, and decisions. Accuracy is a priority"},
                {
                    "role": "user",
                    "content":  f'''{text_content}\n\n
                        1. Give a one-paragraph summary of the key topics and discussions had during the meeting. Describe the state, city and date of the meeting.
                        2. Give me a 2 page summary of the key sections using these guidelines:
                        - Use a clear, descriptive header for each section of the meeting. If timestamps are included in the transcript, then include the timestamp for when that section began.
                        - Be sure to particularly focus on capturing notable announcements at the beginning of the meeting and public commentary/Q&As, either throughout the meeting or in dedicated sections at the end.
                        - Provide 4-6 detailed bullet points with each containing 2-3 sentences that capture notable points that journalists and community members would want to know, such as:
                            - Specific goals of initiatives or projects
                            - Numeric data points (e.g., budget figures, timelines, statistics)
                            - Key arguments or rationales presented
                            - Notable quotes from participants (with attribution)
                            - Specific plans or strategies discussed
                            - Any decisions made or actions taken
                            - Controversies or disagreements, including the perspectives of different sides
                        - For each proposal or concern raised:
                            - Clearly state the specific proposal or issue
                            - Provide cost estimates or budget implications if mentioned
                            - Outline the pros and cons discussed
                            - Mention any alternatives suggested
                        - For public comments or concerns:
                            - Explain the context or background of the concern
                            - Detail any specific requests or demands made by the public
                            - Include the response from officials or relevant parties, if any
                        - Highlight discussions that will have a significant impact on affected communities.
                        - For contentious issues, clearly outline the different viewpoints, approximate size of each group (if mentioned), and the main points of disagreement. 
                        - Provide a separate section for these contentious issues

                        3. Journalistic Leads
                        Suggest 5 potential article ideas for journalists that would help people in the community develop a deeper and more comprehensive understanding of important topics, each with:

                        - A compelling headline
                        - 2-3 sentences explaining the key questions or angles to explore
                        - Specific data points or quotes from the meeting that support the story's importance — use only direct quotes from the transcript with no editing at all.

                        '''
                }
            ]
        )
        summary = completion.choices[0].message.content
    except Exception as e:
        return jsonify({"error": f"Failed to generate summary: {e}"}), 500

    # Send the summary to the Slack webhook
    payload = {
        "Doc_link": summary
    }

    slack_response = requests.post(WEBHOOK_URL, json=payload)

    if slack_response.status_code == 200:
        return jsonify({"message": "Summary sent successfully!"}), 200
    else:
        return jsonify({"error": f"Failed to send summary. Status code: {slack_response.status_code}"}), slack_response.status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
