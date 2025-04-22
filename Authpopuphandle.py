from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
import time
from webdriver_manager.chrome import ChromeDriverManager

service= Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

#this type of authentication doesnot have any html so we cannot handle using driverfindelement or alert so we must directly provi
#de the username and passsowrd in the url
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")

time.sleep(5)
driver.quit()