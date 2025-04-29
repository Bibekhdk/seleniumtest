from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import pytest

driver = None

@pytest.fixture(scope="module")
def init_driver():
    global driver
    print("----------------setup------------")
    service = Service(ChromeDriverManager().install())
    driver= webdriver.Chrome(service=service)
    driver.implicitly_wait(10)
    driver.delete_all_cookies()
    driver.get("https://www.google.com")

    yield
    print("----------------teardown------------")
    driver.quit()

@pytest.mark.usefixtures("init_driver")
def test_google_title():
    assert driver.title =="Google"

@pytest.mark.usefixtures("init_driver")
def test_google_url():
    assert driver.current_url =="https://www.google.com/"
    assert "Google" in driver.title
    


