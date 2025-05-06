import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

@pytest.fixture(params=['chrome','firefox'],scope='class')
def init_driver(request):
     if request.param=="chrome":
        service=Service(ChromeDriverManager().install())
        web_driver= webdriver.Chrome(service=service)
     if request.param=="firefox":
        service=Service("/snap/bin/geckodriver")
        web_driver = webdriver.Firefox(service=service)

     request.cls.driver=web_driver
     yield
     web_driver.quit()
