from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import pytest
from pages.categories_page import CategoriesPage
from utils.driver_factory import get_driver

@pytest.fixture
def driver():
    driver = get_driver("chrome") 
    driver.get("https://www.navigator.ba/#/categories")
    yield driver
    driver.quit()

def test_categories_is_displayed(driver):
    """
    Test to verify that categories section is loaded correctly
    """
    categories_page = CategoriesPage(driver)
    categories_page.wait_for_categories_to_load()

    # Verify that categories section is visible
    assert driver.find_element(*categories_page.categories_list).is_displayed()

