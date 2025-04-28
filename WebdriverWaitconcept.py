from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
import time

service=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://app.hubspot.com/login")


wait = WebDriverWait(driver,10)

wait.until(Ec.title_contains("HubSpot Login and Sign in"))
print(driver.title)

email_id=wait.until(Ec.presence_of_element_located((By.ID,'username')))
email_id.send_keys("rmm@gmail.com")

driver.quit()