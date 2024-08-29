import pytest
from utils.data_generator import generate_user_data
from utils.api_requests import APIRequests
from utils.links import Links
from pages.base_page import BasePage
from locators.profile_page_locators import ProfilePageLocators
from locators.main_page_locators import MainPageLocators
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(params=['firefox', 'chrome'])
def driver(request):
    browser = None
    if request.param == 'firefox':
        browser = webdriver.Firefox()
        browser.set_window_size(1920, 1080)
    elif request.param == 'chrome':
        options = Options()
        options.add_argument('--window-size=1920,1080')
        browser = webdriver.Chrome(options=options)
    browser.get(Links.BASE_URL)

    yield browser

    browser.quit()


@pytest.fixture
def user():
    user_data = generate_user_data()
    api_client = APIRequests()

    response = api_client.create_user(
        email=user_data['email'],
        password=user_data['password'],
        name=user_data['name']
    )

    yield user_data

    access_token = response.json()['accessToken'].split(' ')[1]
    api_client.delete_user(access_token)


@pytest.fixture
def login(driver, user):
    login_page = BasePage(driver)
    login_page.find_clickable_element(MainPageLocators.PROFILE_BUTTON).click()
    login_page.find_visible_element_located(ProfilePageLocators.EMAIL_INPUT_FIELD)
    login_page.send_keys(ProfilePageLocators.EMAIL_INPUT_FIELD, user['email'])
    login_page.send_keys(ProfilePageLocators.PASSWORD_INPUT_FIELD, user['password'])
    login_page.find_clickable_element(ProfilePageLocators.LOGIN_BUTTON).click()
