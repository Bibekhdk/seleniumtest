from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time

service=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=service)

driver.get("https://demoqa.com/upload-download")

# note: there must be 'type=file' in the upload or browse file button otherwise it wont work 


driver.find_element(By.ID,"uploadFile").send_keys("/home/bibek-hadkhale/Downloads/pexels-kovyrina-937980.jpg")


time.sleep(5)
driver.quit()
