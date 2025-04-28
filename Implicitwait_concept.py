from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://app.hubspot.com/login")

driver.implicitly_wait(10)

# this give max time out period = 10seconds and it is also called as dyanamic wait
# implicitly wait will apply for all the webelements available in the page
#also called as global wait
#is applied for find_elements and find_element
# it is only for web elements
#except webelements like  title,url,alert etc we use explicit wait 
driver.find_element(By.ID,'username').send_keys("hello@fgamil.com")

time.sleep(5)
driver.quit()
