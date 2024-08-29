from pages.profile_page import ProfilePage
from locators.profile_page_locators import ProfilePageLocators
from locators.main_page_locators import MainPageLocators
from utils.links import Links
from utils.expected_results import ExpectedResults
import allure


class TestProfile:

    @allure.title('Проверка перехода по клику в Личный кабинет')
    def test_transfer_to_profile_page(self, driver, login):
        profile_page = ProfilePage(driver)
        profile_page.find_visible_element_located(MainPageLocators.PROFILE_BUTTON)
        profile_page.click_go_to_profile()
        profile_page.find_visible_element_located(ProfilePageLocators.PROFILE_SECTION)
        current_page = profile_page.get_current_url()
        assert current_page == Links.PROFILE

    @allure.title('Проверка перехода в раздел История заказов на странице профиля')
    def test_transfer_to_order_history(self, driver, login):
        profile_page = ProfilePage(driver)
        profile_page.find_visible_element_located(MainPageLocators.PROFILE_BUTTON)
        profile_page.click_go_to_profile()
        profile_page.find_visible_element_located(ProfilePageLocators.ORDERS_HISTORY_SECTION)
        profile_page.click_to_order_history()
        current_page = profile_page.get_current_url()
        assert current_page == Links.ORDER_HISTORY

    @allure.title('Проверка выхода из аккаунта')
    def test_user_logout(self, driver, login):
        profile_page = ProfilePage(driver)
        profile_page.find_visible_element_located(MainPageLocators.PROFILE_BUTTON)
        profile_page.click_go_to_profile()
        profile_page.find_visible_element_located(ProfilePageLocators.LOGOUT_LINK)
        profile_page.click_logout_link()
        profile_page.find_visible_element_located(ProfilePageLocators.LOGIN_BUTTON)
        assert profile_page.get_current_text(ProfilePageLocators.LOGIN_BUTTON) == ExpectedResults.LOGIN
