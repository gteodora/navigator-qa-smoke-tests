from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.page_title = (By.TAG_NAME, "title")

    def check_homepage_title(self):
        title = self.driver.find_element(*self.page_title).text
        print(f"Page title is: {title}")
