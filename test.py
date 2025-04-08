from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
import time
import random

def setup_driver():
    options = Options()
    options.binary_location = "/usr/bin/microsoft-edge-stable"  # Path to Edge
    options.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/120.0.0.0")
    options.add_argument("--disable-blink-features=AutomationControlled")  # Prevent bot detection
    options.add_argument("--disable-infobars")  # Disable info bars
    options.add_argument("--start-maximized")  # Start maximized

    service = Service("/usr/local/bin/msedgedriver")  # Path to WebDriver
    driver = webdriver.Edge(service=service, options=options)
    return driver

# Automate Login on Quizlet (Edge on Ubuntu)
def test_login(username, password):
    driver = setup_driver()
    driver.get("https://quizlet.com/login")  
    time.sleep(5)  # Wait for page to load

    try:
        driver.find_element(By.NAME, "username").send_keys(username)
        time.sleep(random.uniform(2, 4))  # Random delay
        driver.find_element(By.NAME, "password").send_keys(password)
        time.sleep(random.uniform(2, 4))  # Random delay

        driver.find_element(By.XPATH, "//button[contains(text(),'Log in')]").click()
        time.sleep(8)  # Wait for response

        if "dashboard" in driver.current_url:
            print("✅ Login Successful!")
        else:
            print("❌ Login Failed!")

    except Exception as e:
        print(f"⚠️ Error: {e}")

    finally:
        time.sleep(15)  # Keep browser open for manual interaction
        driver.quit()

# Test with sample credentials
test_login("your_username", "your_password")
