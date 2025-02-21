from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Chrome options for running headless (without a GUI)
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")  # 某些环境下需要禁用 GPU
chrome_options.add_argument("--no-sandbox") # 避免权限问题
chrome_options.add_argument("--disable-dev-shm-usage") #  /dev/shm is too small in certain docker environments

# Path to chromedriver (since it's in /usr/local/bin, no need to specify)
driver = webdriver.Chrome(options=chrome_options)

try:
    # 1. Navigate to the website
    driver.get("https://www.example.com")  # Replace with your website URL
    print("Opened website successfully.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # 6. Close the browser
    driver.quit()
    print("Browser closed.")
