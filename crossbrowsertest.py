from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.service import Service as ChromeService
import time

browsername = "chrome"  

if browsername == "firefox":
    # service = FirefoxService(GeckoDriverManager().install())
    # driver = webdriver.Firefox(service=service) i have commented this beacause in ubuntu the firefox driver cause some eroor in this code so we put another code whic is below

    service = Service("/snap/bin/geckodriver")  # Use snap's geckodriver
    driver = webdriver.Firefox(service=service)

elif browsername == "chrome":
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
else:
    print("Enter the correct browser name:", browsername)






    
    exit()

driver.implicitly_wait(5)
driver.get("https://ipn-tms-staging.koilifin.com/auth")

driver.find_element(By.NAME, "username").send_keys("admin1")
driver.find_element(By.NAME, "password").send_keys("@dmin2929A")
driver.find_element(By.CLASS_NAME, "css-nxzcop").click() 
print(driver.title)

time.sleep(5)
driver.quit()
