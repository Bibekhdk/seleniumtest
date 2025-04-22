from selenium import webdriver
from selenium.webdriver import ActionChains
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()

url = "https://demoqa.com"
driver.get(url)


widgets_card = driver.find_element(By.XPATH, "//div[@class='card-body']/h5[text()='Widgets']/ancestor::div[@class='card mt-4 top-card']")
widgets_card.click()


tool_tips = driver.find_element(By.XPATH, "//span[text()='Tool Tips']/ancestor::li")

# Scroll to "Tool Tips" in sidebar and click
driver.execute_script("arguments[0].scrollIntoView();", tool_tips)
time.sleep(1)
tool_tips.click()


# Wait and perform hover using action chains
tooltip_button = driver.find_element(By.ID, "toolTipButton")
actions = ActionChains(driver)
actions.move_to_element(tooltip_button).perform()



time.sleep(5)
driver.quit()
