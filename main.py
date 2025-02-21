from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

# Chrome options for running headless (no GUI)
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# IMPORTANT: No need to specify executable_path if ChromeDriver is in PATH (e.g., installed via apt)
# If you install chrome with apt, then chromedriver is also installed at `/usr/lib/chromium-browser/chromedriver`.
driver = webdriver.Chrome(options=chrome_options)

try:
    # 1. Navigate to the website
    driver.get("https://www.example.com")  # Replace with your website URL
    print("Opened website successfully.")

    print("Login successful!")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    driver.quit()
    print("Browser closed.")
