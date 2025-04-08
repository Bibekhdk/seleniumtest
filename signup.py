from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Initialize WebDriver
def setup_driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    return driver

# Automate Signup on Quizlet
def test_signup():
    driver = setup_driver()
    driver.get("https://quizlet.com/sign-up")  # Open signup page
    time.sleep(20)

    try:
        # Fill in the Signup form
        driver.find_element(By.NAME, "username").send_keys("testuser123")
        driver.find_element(By.NAME, "email").send_keys("testuser123@gmail.com")
        driver.find_element(By.NAME, "password").send_keys("Test@12345")

        # Click on "Sign up"
        driver.find_element(By.XPATH, "//button[contains(text(),'Sign up')]").click()
        time.sleep(5)

        # Verification: Check if signup was successful
        if "dashboard" in driver.current_url:
            print("✅ Signup successful!")
        else:
            print("❌ Signup failed!")

    except Exception as e:
        print(f"⚠️ Error occurred: {e}")

    finally:
        driver.quit()

# Run the signup test
test_signup()
