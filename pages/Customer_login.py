from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.locators import login_locators as loc



class CustomerLogin(BasePage):
    page_url = '/auth/login'

    def login_form(self, login, password):
        email_field = self.find(loc.email_field_locator)
        password_field = self.find(loc.password_field_locator)
        button = self.find(loc.button_locator)
        email_field.send_keys(login)
        password_field.send_keys(password)
        button.click()

    def check_error(self, text):
        login_error = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '[data-test="login-error"]')))
        # login_error = driver.find_element(By.CSS_SELECTOR, '[data-test="login-error"]')
        assert login_error.text == text
