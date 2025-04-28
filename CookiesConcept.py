from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get("https://www.reddit.com/")
print(driver.get_cookies())
driver.add_cookie({"name":"bibekpython","domain":"reddit.com","value":"python"})


cookies = driver.get_cookies()


for cook in cookies:
    print(cook)