from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.password_recovery_locators import PasswordRecoveryLocators
import allure


class PasswordRecoveryPage(BasePage):

    @allure.step('Нажать на Восстановить пароль')
    def click_on_recovery_password_link(self):
        return self.find_clickable_element(PasswordRecoveryLocators.RESTORE_PASSWRD_LINK).click()

    @allure.step('Ввести почту для восстановления пароля')
    def fill_email_for_recovery(self, email):
        return self.find_element_located(PasswordRecoveryLocators.EMAIL_INPUT_FIELD).send_keys(email)

    @allure.step('Нажать на кнопку Восстановить')
    def click_on_recovery_button(self):
        return self.find_clickable_element(PasswordRecoveryLocators.RECOVERY_PASSWRD_BUTTON).click()

    @allure.step('Нажать на кнопку Войти в аккаунт')
    def click_login_button_on_main_page(self):
        return self.find_clickable_element(MainPageLocators.AUTH_BUTTON_ON_MAIN_PAGE).click()

    @allure.step('Нажать на кнопку Показать/скрыть пароль')
    def click_show_password(self):
        return self.find_clickable_element(PasswordRecoveryLocators.SHOW_PASSWORD_BUTTON).click()

    @allure.step('Найти активное поле Пароль')
    def find_active_password_field(self):
        return self.find_element_located(PasswordRecoveryLocators.ACTIVE_PASSWORD_INPUT_FIELD)

    @allure.step('Ввести новый пароль для восстановления УЗ')
    def fill_new_password_for_recovery(self, password):
        return self.find_element_located(PasswordRecoveryLocators.PASSWORD_INPUT_FIELD).send_keys(password)
