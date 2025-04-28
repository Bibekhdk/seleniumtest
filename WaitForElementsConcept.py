from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
import time


service=Service(ChromeDriverManager().install())
driver= webdriver.Chrome(service=service)


driver.get("https://www.freshworks.com/")

wait=WebDriverWait(driver,10)
Footer_Links =wait.until(Ec.presence_of_all_elements_located((By.CSS_SELECTOR,"footer li")))
print(len(Footer_Links))


#we can also use other ec features such as
wait.until(Ec.frame_to_be_available_and_switch_to_it((By.ID,'test')))
wait.until(Ec.element_located_to_be_selected(('checkbox')))
wait.until(Ec.url_contains('freshworks'))


time.sleep(5)
driver.quit()