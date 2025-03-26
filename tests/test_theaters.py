import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.theaters_page import TheatersPage
from utils.driver_factory import get_driver

@pytest.fixture
def driver():
    # Setup WebDriver (replace with your actual driver path)
    driver = get_driver("chrome") 
    driver.get("https://www.navigator.ba/#/list/sarajevska-pozorista")
    yield driver
    driver.quit()

def test_theaters_is_displayed(driver):
    """
    Test to verify that theaters list is loaded correctly
    """
    theaters_page = TheatersPage(driver)
    theaters_page.wait_for_theaters_to_load()

    # Verify that theater list is visible
    assert driver.find_element(*theaters_page.theaters_list).is_displayed()

def test_theaters_load(driver):
    """
    Test to verify that the theaters list loads correctly.
    """
    theaters_page = TheatersPage(driver)
    theaters_page.wait_for_theaters_to_load()

    # Get all theaters
    theater_list = theaters_page.get_theaters()

    # Verify that at least one theater is loaded
    assert len(theater_list) > 0, "No theaters were found on the page"


def test_click_narodno_pozoriste(driver):
    """
    Test to verify that clicking 'Narodno pozorište' changes the page title.
    """
    theaters_page = TheatersPage(driver)
    theaters_page.wait_for_theaters_to_load()

    theater_list = theaters_page.get_theaters()
    if len(theater_list) > 0 and 'Narodno pozorište' in theater_list:
        # Click on 'Narodno pozorište'
        theaters_page.click_theater("Narodno pozorište")

        # Wait for title change
        WebDriverWait(driver, 10).until(EC.title_contains("Narodno pozorište"))

        # Verify that the title has changed
        assert "Narodno pozorište" in driver.title 
    
