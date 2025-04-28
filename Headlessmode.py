from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options


import time 

options = Options()
options.add_argument("--incognito")
options.add_argument("--headless")

#for chrome browser
# service = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service, options=options)
# driver.maximize_window()


#for firefox browser
service = Service("/snap/bin/geckodriver")
driver= webdriver.Firefox(service=service, options=options)
driver.maximize_window()


driver.get("https://www.google.com")
print(driver.title)
driver.quit()

