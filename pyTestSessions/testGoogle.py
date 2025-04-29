from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import pytest

def test_google():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("https://www.google.com")
    assert driver.title=="Google"
    driver.quit()


def test_youtube():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("https://www.youtube.com")
    assert driver.title=="youtube   "
    driver.quit()


def test_gmail():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("https://mail.google.com/mail")
    assert driver.title=="Inbox (144) - abcbibek246@gmail.com - Gmail"
    driver.quit()


def test_github():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("https://github.com/")
    assert driver.title=="Github"
    driver.quit()



