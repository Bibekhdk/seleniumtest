from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://ipn-tms-staging.koilifin.com")
time.sleep(20)
 
print("Title is:", driver.title)

elem = driver.find_element(By.NAME,"q")

elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "no result found" not in driver.page_source

driver.close()