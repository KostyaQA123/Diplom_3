from pages.profile_page import ProfilePage
from utils.links import Links
from utils.expected_results import ExpectedResults
import allure


class TestProfile:

    @allure.title('Проверка перехода по клику в Личный кабинет')
    def test_transfer_to_profile_page(self, driver, login):
        profile_page = ProfilePage(driver)
        profile_page.click_go_to_profile()
        profile_page.wait_for_profile_section()
        current_page = profile_page.get_current_url()
        assert current_page == Links.PROFILE

    @allure.title('Проверка перехода в раздел История заказов на странице профиля')
    def test_transfer_to_order_history(self, driver, login):
        profile_page = ProfilePage(driver)
        profile_page.click_go_to_profile()
        profile_page.click_to_order_history()
        current_page = profile_page.get_current_url()
        assert current_page == Links.ORDER_HISTORY

    @allure.title('Проверка выхода из аккаунта')
    def test_user_logout(self, driver, login):
        profile_page = ProfilePage(driver)
        profile_page.click_go_to_profile()
        profile_page.click_logout_link()
        profile_page.wait_for_login_page()
        login_button_text = profile_page.get_login_button_text()
        assert login_button_text == ExpectedResults.LOGIN
