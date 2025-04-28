from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


options=Options()
options.add_argument("--headless")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service,options=options)
driver.maximize_window()



#for full page screenshot we have to use in headless mode 
driver.get("https://www.google.com")
scroll_width = driver.execute_script("return document.body.scrollWidth")
scroll_height = driver.execute_script("return document.body.scrollHeight")
driver.set_window_size(scroll_width, scroll_height)

driver.find_element(By.TAG_NAME,'body').screenshot('google_fullpage_ss.png')


driver.quit()