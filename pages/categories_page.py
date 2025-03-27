from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CategoriesPage:
    def __init__(self, driver):
        self.driver = driver
        # Locator for the categories section
        self.categories_list = (By.CSS_SELECTOR, "ul.menu_content_list.categories")  
        self.category_items = (By.CSS_SELECTOR, "li.list-item")
        self.category_links = (By.CSS_SELECTOR, "li.ember-view.list-item a")  

    def wait_for_categories_to_load(self):
        """
        Wait for the categories section to be visible on the page
        """
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.categories_list)
        )

    def get_category_items(self):
        """
        Get all the category items listed on the page
        """
        return self.driver.find_elements(*self.category_items)


    def click_category(self, category_name):
        """
        Click on a category by its name
        """
        categories = self.get_category_items()
        for category in categories:
            if category_name in category.text:
                category.click()
                break


