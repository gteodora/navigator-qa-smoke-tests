import pytest
from selenium import webdriver
from pages.homepage_page import HomePage
from utils.driver_factory import get_driver

@pytest.fixture
def driver():
    driver = get_driver("chrome")  
    driver.get("https://www.navigator.ba")
    yield driver
    driver.quit()

def test_homepage_loads(driver):
    homepage = HomePage(driver)
    homepage.check_homepage_title() 
    assert "Navigator" in driver.title 
