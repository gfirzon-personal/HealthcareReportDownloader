from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up Chrome options
chrome_options = Options()

# Headless mode is a way of running a web browser without a graphical user interface (GUI). This allows the browser to operate in the background, which is useful for automated tasks such as web scraping, testing, and other automation tasks where you do not need to see the browser window.
# In headless mode, the browser performs all the same operations as it would in normal mode, but it does not display any visual output. This can make automated tasks faster and more efficient, as it reduces the overhead associated with rendering the GUI.
chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument("--no-sandbox")  # Required when running as root
chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
chrome_options.add_argument("--disable-gpu")  # Applicable for some environments
chrome_options.add_argument("--remote-debugging-port=9222")  # Debugging

chrome_options.add_experimental_option('prefs', {
    #"download.default_directory": r"C:\path\to\your\download\directory",  # Change this to your download directory
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
})

# Set up the WebDriver
# service = Service('C:\\WebDriver\\bin\\chromedriver.exe')  # Change this to the path of your chromedriver
service = Service('/usr/local/bin/chromedriver')  # Change this to the path of your chromedriver
driver = webdriver.Chrome(service=service, options=chrome_options)

button = None
try:
    # Navigate to the URL
    driver.get('https://340bopais.hrsa.gov/reports')

    # Wait for the button to be clickable and click it
    wait = WebDriverWait(driver, 20)
    print("Waiting for the button to be clickable...")
    button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[title='Click here to download the Contract Pharmacy Daily Report']")))
    print("Button found. Clicking the button...")    
    button.click()

    # Wait for the download to complete
    time.sleep(120)  # Adjust the sleep time if necessary
except Exception as e:
    print('Button not found')
    print(button)
finally:
    # Close the browser
    driver.quit()