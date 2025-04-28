from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
import time

service = Service(ChromeDriverManager().install())
driver= webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://demoqa.com/alerts")

driver.find_element(By.XPATH,"//button[@id='alertButton']").click()


try:
    wait = WebDriverWait(driver, 10)
    alert = wait.until(Ec.alert_is_present())
    print("Alert Text:", alert.text)
    alert.accept()
except:
    print("No browser alert present")


driver.quit()