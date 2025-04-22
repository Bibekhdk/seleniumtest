from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

service=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get("https://demoqa.com/droppable")

source = driver.find_element(By.ID,"draggable")
target = driver.find_element(By.ID,"droppable")

#now using drag and drop feature using Actionchains 

act_chains = ActionChains(driver)
# act_chains.drag_and_drop(source,target).perform()

# we can also use specific actions as click hold drop type 

act_chains.click_and_hold(source).move_to_element(target).release().perform()

time.sleep(5)
driver.quit()