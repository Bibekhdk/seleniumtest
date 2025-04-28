from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains,DesiredCapabilities
from selenium.webdriver.support import expected_conditions as Ec
from webdriver_manager.firefox import GeckoDriverManager

import time

# one option is this:
# options = Options()
# options.add_argument("--allowing-running-insecure-content")
# options.add_argument("--ignore-certificate-errors")


#another option but it is not used in newer selenium verisons :
# desired_capabilities = DesiredCapabilities().CHROME.copy()
# desired_capabilities["acceptInsecureCerts"]=True

#service= Service(ChromeDriverManager().install())
#driver= webdriver.Chrome(service=service,options=options)
#driver=webdriver.Chrome(service=service,desired_capabilities=desired_capabilities)

#best way is for chrome:
# options =Options()
# options.set_capability("acceptInsecureCerts",True)
# service= Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service,options=options)
# driver.implicitly_wait(10)


#for firefox:
options = Options()
options.accept_insecure_certs = True   #we can also do using desiredcapabilties but newer selenium dont use that

service = Service("/snap/bin/geckodriver")
driver=webdriver.Firefox(service=service)   

driver.get("https://untrusted-root.badssl.com/")
print(driver.find_element(By.TAG_NAME,'h1').text)

time.sleep(3)
driver.quit()