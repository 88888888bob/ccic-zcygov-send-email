from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service # 导入 Service 类
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Chrome options for running headless (no GUI)
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# ChromeDriver 的路径 (使用 apt 安装时，通常在这里)
chrome_driver_path = "/usr/lib/chromium-browser/chromedriver"

# 创建 Service 对象，指定 ChromeDriver 的路径
service = Service(executable_path=chrome_driver_path)

# 初始化 Chrome WebDriver，并传入 Service 对象
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # 1. Navigate to the website
    driver.get("https://www.example.com")  # Replace with your website URL
    print("Opened website successfully.")


except Exception as e:
    print(f"An error occurred: {e}")

finally:
    driver.quit()
    print("Browser closed.")
