To achieve this, you can use the `selenium` library in Python to automate the browser actions. Here is a step-by-step plan and the corresponding code:

1. Install the necessary libraries.
2. Set up the Selenium WebDriver.
3. Navigate to the specified URL.
4. Locate the button by its title attribute.
5. Simulate a click on the button to download the file.

### Step 1: Install the necessary libraries
```sh
pip install selenium
```

### Step 2: Set up the Selenium WebDriver and automate the download
```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up Chrome options
chrome_options = Options()
chrome_options.add_experimental_option('prefs', {
    "download.default_directory": r"C:\path\to\your\download\directory",  # Change this to your download directory
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
})

# Set up the WebDriver
service = Service('path/to/chromedriver')  # Change this to the path of your chromedriver
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Navigate to the URL
    driver.get('https://340bopais.hrsa.gov/reports')

    # Wait for the button to be clickable and click it
    wait = WebDriverWait(driver, 10)
    button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@title='Click here to download the Contract Pharmacy Daily Report']")))
    button.click()

    # Wait for the download to complete
    time.sleep(10)  # Adjust the sleep time if necessary

finally:
    # Close the browser
    driver.quit()
```

### Notes:
- Make sure to replace `path/to/chromedriver` with the actual path to your ChromeDriver executable.
- Adjust the download directory path to your desired location.
- The `time.sleep(10)` is a simple way to wait for the download to complete. You might want to implement a more robust solution to check for the file's existence.

This script will open a Chrome browser, navigate to the specified URL, find the button with the given title attribute, click it, and download the file to the specified directory.

Similar code found with 1 license type