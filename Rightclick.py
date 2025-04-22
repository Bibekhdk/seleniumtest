from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get("https://demoqa.com/buttons")

right_click_btn_ele = driver.find_element(By.XPATH,"//button[@id='rightClickBtn']")
act_chain = ActionChains(driver)
act_chain.context_click(right_click_btn_ele).perform()



double_click_btn_ele= driver.find_element(By.XPATH,'//button[@id="doubleClickBtn"]')
act_chain.double_click(double_click_btn_ele).perform()








time.sleep(5)
driver.quit()