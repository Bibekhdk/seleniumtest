from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.service import Service as ChromeService
import time

browsername = "firefox"

if browsername == "firefox":
    service = FirefoxService(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
elif browsername == "chrome":
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
else:
    print("Enter the correct browser name: " + browsername)
    exit()

driver.implicitly_wait(5)
driver.get("https://ipn-tms-staging.koilifin.com/auth")

#  Correct the class selector: remove the dot in find_element(By.CLASS_NAME)
driver.find_element(By.NAME, "username").send_keys("admin1")
driver.find_element(By.NAME, "password").send_keys("@dmin2929A")
driver.find_element(By.CLASS_NAME, "css-nxzcop").click()  # <-- FIXED

print(driver.title)

time.sleep(5)
driver.quit()
