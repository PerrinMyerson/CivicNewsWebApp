from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
import time

# URL of the target website
url = "https://learndoe.org/pep/archive-pep-oct30-2024/"

# Number of refresh attempts
max_attempts = 3

# Path to the ChromeDriver (ensure it's in your PATH or provide the full path)
service = Service("path/to/chromedriver")
driver = webdriver.Chrome(service=service)

# Open the target website
driver.get(url)
actions = ActionChains(driver)

# Main loop to check and refresh
for attempt in range(1, max_attempts + 1):
    print(f"Attempt {attempt} of {max_attempts}...")

    # Simulate Shift + T to toggle subtitles
    actions.key_down(Keys.SHIFT).send_keys('t').key_up(Keys.SHIFT).perform()
    time.sleep(2)  # Allow time for the subtitles to load

    # Check network requests for the VTT file
    logs = driver.execute_script("return window.performance.getEntries();")
    vtt_files = [entry['name'] for entry in logs if '.vtt' in entry['name']]
    
    if vtt_files:
        print("VTT file found:")
        print(vtt_files)
        break
    else:
        print("VTT file not found. Waiting 5 seconds before refreshing...")
        time.sleep(5)
else:
    print("VTT file not found after 3 attempts.")

# Close the browser
driver.quit()
