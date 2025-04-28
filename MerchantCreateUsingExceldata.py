from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

# Load Excel file with credentials
df = pd.read_excel("logincredential3.xlsx")
url = df.loc[0, 'url']
username = df.loc[0, 'username']
password = df.loc[0, 'password']
accountnumber = df.loc[0, 'AccountNumber']
merchantpan = df.loc[0, 'MerchantPan']
branchbtn = df.loc[0, 'Branch']
schemebox = df.loc[0, 'Scheme']
nchl = df.loc[0, 'NCHL']
categorycode = df.loc[0, 'CategoryCode']
namebtn = df.loc[0, 'Name']
emailbtn = df.loc[0, 'Email']
addressbtn = df.loc[0, 'Address']
phonefill = df.loc[0, "Phone"]


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
# driver.implicitly_wait(10)
wait = WebDriverWait(driver, 15)


driver.get(url)


username_btn = driver.find_element(By.NAME, "username")
password_btn = driver.find_element(By.NAME, "password")
submit_btn = driver.find_element(By.XPATH, "//button[@id='submit-button']")

username_btn.send_keys(username)
password_btn.send_keys(password)
submit_btn.click()

# time.sleep(2)

merchant_viewbtn = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Merchant')]")))
merchant_viewbtn.click()


addmerchant_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Add Merchant']")))
addmerchant_btn.click()
# time.sleep(10)


account_number = wait.until(EC.presence_of_element_located((By.ID, "account_number")))
account_number.send_keys(str(accountnumber))


merchant_pan = driver.find_element(By.ID, "pan")
merchant_pan.send_keys(str(merchantpan))


branch_btn = wait.until(EC.presence_of_element_located((By.ID, "branch")))
branch_btn.click()
branch_btn.send_keys(branchbtn)
time.sleep(1)
branch_btn.send_keys(Keys.DOWN)
branch_btn.send_keys(Keys.ENTER)


scheme_input = wait.until(EC.presence_of_element_located((By.ID, "scheme-select-box")))
scheme_input.click()
scheme_input.send_keys(schemebox)
time.sleep(1)
scheme_input.send_keys(Keys.DOWN)
scheme_input.send_keys(Keys.ENTER)


nchl_input = wait.until(EC.presence_of_element_located((By.NAME, "nchl_merchantCode")))
nchl_input.send_keys(nchl)
time.sleep(1)


categorycode_btn = wait.until(EC.presence_of_element_located((By.ID, "category-code-search")))
categorycode_btn.click()
time.sleep(1)
categorycode_btn.send_keys(Keys.DOWN)
categorycode_btn.send_keys(Keys.ENTER)


name_btn = driver.find_element(By.ID, "name")
name_btn.send_keys(namebtn)

email_btn = driver.find_element(By.ID, "email")
email_btn.send_keys(emailbtn)

address_btn = driver.find_element(By.ID, "address")
address_btn.send_keys(addressbtn)

phone_btn = driver.find_element(By.ID, "phone")
phone_btn.send_keys(str(phonefill))

time.sleep(5)


submit_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
submit_btn.click()

time.sleep(5)
driver.quit()
