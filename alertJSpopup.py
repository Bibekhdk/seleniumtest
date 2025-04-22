from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
import time

service=Service(ChromeDriverManager().install())
driver= webdriver.Chrome(service=service)
driver.maximize_window()

driver.get("https://demoqa.com/alerts")


#handling alert popup
alert_button=driver.find_element(By.ID,"alertButton")
alert_button.click()
time.sleep(3)


alert_button= driver.switch_to.alert
print(alert_button.text)
alert_button.accept()  #accepting it by clicking ok button
# alert.dismiss()  #dismissig it by canceling it
driver.switch_to.default_content() #helps to switch to normal page after the popup disappears
time.sleep(5)

alert_confirm_btn= driver.find_element(By.ID,"confirmButton")
alert_confirm_btn.click()
time.sleep(5)

alert_confirm_btn=driver.switch_to.alert
print(alert_confirm_btn.text)
alert_confirm_btn.accept()  
driver.switch_to.default_content()



prompt_btn = driver.find_element(By.ID,"promtButton")
prompt_btn.click()
time.sleep(2)

prompt_btn = driver.switch_to.alert
print(prompt_btn.text)
prompt_btn.send_keys("ramhari")
time.sleep(2)
prompt_btn.accept()
driver.switch_to.default_content()



time.sleep(4)
driver.quit()
