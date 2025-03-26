from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TheatersPage:
    def __init__(self, driver):
        self.driver = driver
        # Locators
        self.theaters_list = (By.CSS_SELECTOR, "ul.menu_content_list")  
        self.theater_links = (By.CSS_SELECTOR, "li.ember-view.place.art a")  

    def wait_for_theaters_to_load(self):
        """
        Wait until the list of theaters is visible.
        """
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.theaters_list)
        )

    def get_theaters(self):
        """
        Get all the theater elements.
        """
        return self.driver.find_elements(*self.theaters_list)

    def click_theater(self, theater_name):
        """
        Click on a theater by name.
        """
        theaters = self.driver.find_elements(*self.theater_links)
        for theater in theaters:
            if theater_name in theater.text:
                theater.click()
                break
