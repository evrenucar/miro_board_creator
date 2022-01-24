import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def test_driver_manager_chrome():
    service = ChromeService(executable_path=ChromeDriverManager().install())

    driver = webdriver.Chrome(service=service)

    driver.quit()

