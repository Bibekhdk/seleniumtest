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
    print("\n" + "-"*60)
    print(f" Attempting login with:\n   Username: '{username}'\n    Password: '{password}'")

    try:
        username_input = driver.find_element(By.NAME,"username")
        password_input = driver.find_element(By.NAME, "password")



        username_input.clear()
        password_input.clear()
        username_input.send_keys(username)
        password_input.send_keys(password)



        driver.find_element(By.CSS_SELECTOR, ".css-nxzcop").click()
        time.sleep(2)



        # for popup notification
        toast_displayed = False
        try:
            wait = WebDriverWait(driver, 3)
            notification = wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "Toastify__toast-body"))
            )
            text = notification.get_attribute("innerText") or notification.get_attribute("textContent")
            print(f" Notification appeared as: {text}")
            toast_displayed = True
        except:
            pass




        # Inline Error Handling
        if not toast_displayed:
            captured = False
            try:
                error_user = WebDriverWait(driver, 2).until(
                    EC.presence_of_element_located((By.ID, "username-helper-text"))
                )
                print(f"! Inline message: {error_user.text}")
                captured = True
            except:
                pass

            try:
                error_pass = WebDriverWait(driver, 2).until(
                    EC.presence_of_element_located((By.XPATH, "//span[text()='Password is required']"))
                )
                print(f"! Inline message: {error_pass.text}")
                captured = True
            except:
                pass

          


        time.sleep(2)
        if driver.current_url == "https://ipn-tms-staging.koilifin.com/dashboard":
            print(" Login successful!")


    

    except Exception as e:
        print(" Error during login attempt:", e)

    


# Test Cases
login("ram", "ram1234")           # Invalid both
login("dibash", "@dmin2929A")     # Invalid username, valid pass
login("admin1", "dibash11")       # Valid username, invalid pass
login("admin1", "")               # Username filled, password blank
login("", "@dmin2929A")           # Username blank, password filled
login("", "")                     # Both blank
login("admin1", "@dmin2929A")     # Valid both

driver.quit()
