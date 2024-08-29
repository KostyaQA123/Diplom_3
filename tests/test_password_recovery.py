from utils.links import Links
from utils.expected_results import TestData
from locators.password_recovery_locators import PasswordRecoveryLocators
from pages.password_recovery_page import PasswordRecoveryPage
import allure


class TestPasswordRecovery:

    @allure.title('Проверка перехода на страницу восстановления пароля по кнопке Восстановить пароль')
    def test_click_recovery_link_on_main_page(self, driver):
        recovery_page = PasswordRecoveryPage(driver)
        recovery_page.click_login_button_on_main_page()
        recovery_page.click_on_recovery_password_link()
        recovery_page.find_visible_element_located(PasswordRecoveryLocators.RECOVERY_PASSWRD_BUTTON)
        forgot_password_url = recovery_page.get_current_url()
        assert forgot_password_url == Links.FORGOT_PASSWORD

    @allure.title('Проверка ввода почты и клик по кнопке Восстановить')
    def test_fill_email_click_recovery(self, driver):
        recovery_page = PasswordRecoveryPage(driver)
        recovery_page.go_to_site(Links.RESET_PASSWORD)
        recovery_page.find_visible_element_located(PasswordRecoveryLocators.RECOVERY_PASSWRD_BUTTON)
        recovery_page.fill_email_for_recovery(TestData.EMAIL)
        recovery_page.click_on_recovery_button()
        recovery_page.find_visible_element_located(PasswordRecoveryLocators.PASSWORD_INPUT_FIELD)
        recovery_url = recovery_page.get_current_url()
        assert recovery_url == Links.RESET_PASSWORD

    @allure.title('Проверка подсветки активного поля ввода пароля при клике на показать/скрыть пароль')
    def test_password_field_highlight_on_switch_visibility(self, driver):
        recovery_page = PasswordRecoveryPage(driver)
        recovery_page.go_to_site(Links.FORGOT_PASSWORD)
        recovery_page.find_visible_element_located(PasswordRecoveryLocators.RECOVERY_PASSWRD_BUTTON)
        recovery_page.fill_email_for_recovery(TestData.EMAIL)
        recovery_page.click_on_recovery_button()
        recovery_page.find_visible_element_located(PasswordRecoveryLocators.PASSWORD_INPUT_FIELD)
        recovery_page.fill_new_password_for_recovery(TestData.PASSWORD)
        recovery_page.click_show_password()
        recovery_page.find_visible_element_located(PasswordRecoveryLocators.ACTIVE_PASSWORD_INPUT_FIELD)
        active_password_field = recovery_page.find_active_password_field()
        assert active_password_field.is_displayed()
