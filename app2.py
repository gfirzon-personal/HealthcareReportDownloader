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
    #"download.default_directory": r"C:\path\to\your\download\directory",  # Change this to your download directory
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
})

# Set up the WebDriver
service = Service('C:\\WebDriver\\bin\\chromedriver.exe')  # Change this to the path of your chromedriver
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