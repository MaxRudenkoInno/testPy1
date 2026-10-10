from selenium.webdriver.common.by import By
from pages.base_page import BasePage

header_title_locator = (By.CSS_SELECTOR, 'h2')

class ProductPage(BasePage):

    page_url = '/category/power-tools'

    def check_title_is(self, title):
        page_title = self.find(header_title_locator)
        assert page_title.text == title