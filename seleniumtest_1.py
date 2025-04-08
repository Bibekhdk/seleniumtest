from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

# Set the path to the ChromeDriver (optional if it's in PATH)
service = Service("/usr/local/bin/chromedriver")

# Initialize the Chrome WebDriver
driver = webdriver.Chrome(service=service)

# Open Google
driver.get("https://www.google.com")

# Print the page title
print("Page Title:", driver.title)

# Wait for a few seconds
time.sleep(5)

# Close the browser
driver.quit()
0