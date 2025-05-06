# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service
# import time
import pytest


# @pytest.fixture(params=['chrome','firefox'],scope='class')
# def init_driver(request):
#     if request.param=="chrome":
#         service=Service(ChromeDriverManager().install())
#         web_driver= webdriver.Chrome(service=service)
#     if request.param=="firefox":
#         service=Service("/snap/bin/geckodriver")
#         web_driver = webdriver.Firefox(service=service)

#     request.cls.driver=web_driver
#     yield
#     web_driver.quit()

@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass

class Test_google(BaseTest):
    def test_google_title(self):
        self.driver.get("https://www.google.com")
        assert self.driver.title=="Google"





