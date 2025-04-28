from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
import time


service=Service(ChromeDriverManager().install())
driver= webdriver.Chrome(service=service)

driver.get("https://app.hubspot.com/login")

wait= WebDriverWait(driver,10)

calssiclogin =wait.until(Ec.element_to_be_clickable((By.LINK_TEXT,"classic login")))
print(calssiclogin.text)
calssiclogin.click()

username= wait.until(Ec.visibility_of_element_located((By.ID,"username")))
username.send_keys("bibek")
time.sleep(5)
driver.quit()