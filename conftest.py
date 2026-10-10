import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.product_page import ProductPage
from pages.Customer_login import CustomerLogin

@pytest.fixture()
def driver():
    options = Options()
    #options.add_argument('--headless')
    browser = webdriver.Chrome(options=options)
    browser.maximize_window()
    browser.implicitly_wait(3)
    yield browser

@pytest.fixture()
def customer_login(driver):
    return CustomerLogin(driver)

@pytest.fixture()
def product_page(driver):
    return ProductPage(driver)

@pytest.fixture
def new_post_id():
    body = {
        "title": "my first post",
        "body": "Body body Body",
        "user_id": 42
    }
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.post(
        'https://jsonplaceholder.typicode.com/posts/',
        json=body,
        headers=headers
    )
    post_id = response.json()['id']
    print(post_id)
    yield post_id
    print('deleting the new post')
    requests.delete(f'https://jsonplaceholder.typicode.com/posts/{post_id}')