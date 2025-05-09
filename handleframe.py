from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver import ActionChains

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get("https://demoqa.com/frames")


#driver.switch_to.frame('frame1')

frame_ele = driver.find_element(By.ID,"frame2")
driver.switch_to.frame(frame_ele)


first_frame = driver.find_element(By.CSS_SELECTOR,"body > h1").text
print(first_frame)

driver.switch_to.default_content()
driver.switch_to.parent_frame()


time.sleep(5)
driver.quit()
