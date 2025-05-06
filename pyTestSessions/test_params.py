from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import pytest

@pytest.mark.usefixtures('init_driver')
class BaseTest:
    pass

class TestHubSpot(BaseTest):
    @pytest.mark.parametrize("username, password",
                             [
                                 ("admin", "admin123"),
                                 ("bibek","bibek123"),

                             ]
                         )
    def test_login(self,username,password):
        """
        this method is used to login
        :param username:
        :param password:
        """
        self.driver.get("https://ipn-tms-staging.koilifin.com/auth")
        self.driver.find_element(By.NAME,"username").send_keys(username)
        self.driver.find_element(By.NAME,"password").send_keys(password)
