from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

url = "https://ipn-tms-staging.koilifin.com/auth"
service = Service('/snap/bin/geckodriver')
driver = webdriver.Firefox(service=service)
driver.get(url)

def login(username, password):
    print(f"Logging in with username: {username} and password: {password}")

    try:
        username_input = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.NAME, "username")))
        password_input = driver.find_element(By.NAME, "password")
        username_input.send_keys(username)
        password_input.send_keys(password)

        driver.find_element(By.CSS_SELECTOR, ".css-nxzcop").click()
        time.sleep(2)

        try:
            wait = WebDriverWait(driver, 3)
            notification = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "Toastify__toast-body")))
            text = notification.get_attribute("innerText")
            print("Login Message:", text)
        except Exception as e:
            print("No login toast or delayed load:", e)

        # Now perform the rest of the navigation
        try:
            merchant_btn = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[1]/main/div/div[1]/div[4]/div/button[1]")))
            merchant_btn.click()

            status_btn = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "status-select")))
            status_btn.click()

            approve_btn = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[3]/ul/li[2]")))
            approve_btn.click()

            action_btn = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[3]/div/div/div/div[2]/div[1]/table/tbody/tr[1]/td[5]/button/svg")))
            action_btn.click()

            viewdetail_btn = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[3]/ul/li/svg")))
            viewdetail_btn.click()

            element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "newcontent")))

            detailedview_btn = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[3]/div/div/div/div[2]/div[1]/div[1]")))
            detailedview_btn.click()

        except Exception as e:
            print("Error during post-login button interactions:", e)

    except Exception as e:
        print("Error during login attempt:", e)

# Call the function to run
login("admin1", "@dmin2929A")

# Close browser
time.sleep(5)
driver.quit()
