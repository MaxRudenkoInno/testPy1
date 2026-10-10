from selenium.webdriver.common.by import By

email_field_locator = (By.ID, 'email')
password_field_locator = (By.ID, 'password')
button_locator = (By.CSS_SELECTOR, '[data-test="login-submit"]')