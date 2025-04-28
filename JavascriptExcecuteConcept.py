from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
import time


service=Service(ChromeDriverManager().install())
driver= webdriver.Chrome(service=service)
driver.implicitly_wait(2)
driver.maximize_window()


driver.get("https://www.freshworks.com/")
demo_btn= driver.find_element(By.LINK_TEXT,"Read the story")
# driver.execute_script("arguments[0].click();",demo_btn)


#in js to print title
# title= driver.execute_script("return document.title;")
# print(title)


# driver.execute_script("history.go(0);")

# driver.execute_script("alert('hello');")

#we can create border around element so i will be helpful while creating bug report and doing ss
# driver.execute_script("arguments[0].style.border='10px solid red'",demo_btn)

# driver.execute_script("window.scrollTo(0,1000)") #for specific pixels as i have given 0 to 1000px


# driver.execute_script("window.scrollTo(0, document.body.scrollHeight)") #scroll to end of page

# driver.execute_script("window.scrollTo( document.body.scrollHeight,0)") #scroll to top of page as it is reverse of bottom

driver.execute_script("arguments[0].scrollIntoView(true);",demo_btn) #this will exceute ethe script till the button  is appered
print(driver.execute_script("return navigator.userAgent;"))

#for sending keys in forms we use value
driver.execute_script("document.getElementById('username').value='hello@gmai.com';")

time.sleep(5)
driver.quit()
