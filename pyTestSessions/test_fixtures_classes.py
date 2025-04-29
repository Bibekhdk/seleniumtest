from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import pytest
import time

@pytest.fixture(scope='class')
def init_chrome_driver(request):
    service = Service(ChromeDriverManager().install())
    ch_driver = webdriver.Chrome(service=service)
    request.cls.driver = ch_driver
    yield
    ch_driver.close()


@pytest.fixture(scope='class')
def init_ff_driver(request):
    service = Service("/snap/bin/geckodriver")
    ff_driver = webdriver.Firefox(service=service)
    request.cls.driver = ff_driver
    yield
    ff_driver.close()

    


