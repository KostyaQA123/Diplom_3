import pytest

from pages.profile_page import ProfilePage
from utils.data_generator import generate_user_data
from utils.api_requests import APIRequests
from utils.links import Links
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
    login_page = ProfilePage(driver)

    login_page.click_go_to_profile()
    login_page.fill_email(user['email'])
    login_page.fill_password(user['password'])
    login_page.click_login_button()
