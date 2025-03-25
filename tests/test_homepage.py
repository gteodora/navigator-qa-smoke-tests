import pytest
from selenium import webdriver
from pages.homepage_page import HomePage
from utils.driver_factory import get_driver

@pytest.fixture
def driver():
    driver = get_driver("chrome")  # Initialize Chrome WebDriver
    driver.get("https://www.navigator.ba")
    yield driver
    driver.quit()

def test_homepage_loads(driver):
    homepage = HomePage(driver)
    homepage.check_homepage_title()  # Custom method from HomePage
    assert "Navigator" in driver.title  # Check that title contains 'Navigator'
