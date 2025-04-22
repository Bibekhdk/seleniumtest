from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get("https://www.apple.com/in/store")

driver.find_element(By.LINK_TEXT,"Mac").click()

driver.back()
time.sleep(5)

driver.forward()
time.sleep(5)

driver.back()
time.sleep(5)

driver.forward()
time.sleep(5)

driver.back()
time.sleep(5)

driver.refresh()

time.sleep(5)
driver.quit()
