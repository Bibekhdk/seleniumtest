from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import random

def random_sleep():
    """Sleep for a random time between 1 and 3 seconds."""
    time.sleep(random.uniform(1, 3))

def setup_driver():
    """Set up the Chrome WebDriver with options."""
    options = webdriver.ChromeOptions()
    # Set the user-agent to mimic a real browser
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5672.63 Safari/537.36")
    # Specify the path to your Chrome user profile
    options.add_argument("user-data-dir=/home/your_username/.config/google-chrome/Default")  # Update your path here
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    return driver

def test_login(username, password):
    """Automate the login process on Quizlet."""
    driver = setup_driver()
    driver.get("https://quizlet.com/login")  # Open the login page
    random_sleep()

    try:
        # Fill in the login form
        driver.find_element(By.NAME, "username").send_keys(username)  # Replace with your username or email
        random_sleep()
        driver.find_element(By.NAME, "password").send_keys(password)  # Replace with your password
        random_sleep()

        # Click on "Log in"
        driver.find_element(By.XPATH, "//button[contains(text(),'Log in')]").click()
        random_sleep()

        # Verification: Check if login was successful
        if "dashboard" in driver.current_url:
            print("✅ Login successful!")
        else:
            print("❌ Login failed!")

    except Exception as e:
        print(f"⚠️ Error occurred: {e}")

    finally:
        driver.quit()  # Close the browser

# Update these credentials with your actual Quizlet credentials
quizlet_username = "your_username_or_email"  # Replace with your Quizlet username or email
quizlet_password = "your_password"  # Replace with your Quizlet password

# Run the login test
test_login(quizlet_username, quizlet_password)
