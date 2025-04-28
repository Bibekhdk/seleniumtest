from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
#driver.implicitly_wait(10)


driver.get("https://ipn-tms-staging.koilifin.com/auth")
usrname_btn = driver.find_element(By.NAME,"username")
usrname_btn.send_keys("bibek1")
password_btn=driver.find_element(By.NAME,"password")
password_btn.send_keys("@dmin2929A")
submit_btn = driver.find_element(By.XPATH,"//button[@id='submit-button']")
submit_btn.click()


time.sleep(2)

merchant_viewbtn = driver.find_element(By.XPATH, "//span[contains(text(), 'Merchant')]")
merchant_viewbtn.click()

addmerchant_btn = driver.find_element(By.XPATH, "//button[text()='Add Merchant']")
addmerchant_btn.click()

time.sleep(15)
driver.quit()
