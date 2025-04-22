from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setting up the driver properly using Service
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)


driver.get('https://www.freshworks.com/')



links_listss= driver.find_elements(By.TAG_NAME,'a')
print(len(links_listss))


for ele in links_listss:
    link_text=ele.text
    print(link_text)
    print(ele.get_attribute('href'))




image_list=driver.find_elements(By.TAG_NAME,"img")
print(len(image_list))


for ele in image_list:
    print(ele.get_attribute('src'))


time.sleep(5)
driver.quit()
