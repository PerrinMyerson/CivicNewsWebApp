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

# Configure Chrome options


# Replace this URL with the desired URL to open
url = "https://learndoe.org/pep/archive-pep-oct30-2024/"

def format_subtitles(subtitles, chunk_size=12):
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

def perform_key_sequence():
    actions = webdriver.ActionChains(driver)
    actions.send_keys("c")
    actions.pause(0.1)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.pause(0.1)
    actions.send_keys(Keys.RETURN)
    actions.perform()

def find_and_click_play_button():
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

def monitor_network_for_vtt():
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
def fetch_transcript():
    try:
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_experimental_option("detach", True)  # Keep browser open after script finishes

    # Initialize the WebDriver with selenium-wire
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        find_and_click_play_button(driver)
        subtitles_text = monitor_network_for_vtt(driver)
        formatted_subtitles = format_subtitles(subtitles_text[7:])
        print(formatted_subtitles)

    except Exception as e:
        formatted_subtitles = f"An error occurred: {e}"

finally:
    # Uncomment to close the browser when done
    # driver.quit()
    pass

# The formatted subtitles are now stored in the `formatted_subtitles` variable
