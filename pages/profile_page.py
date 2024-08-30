from pages.base_page import BasePage
from locators.profile_page_locators import ProfilePageLocators
import allure


class ProfilePage(BasePage):

    @allure.step('Переход на страницу профиля')
    def click_go_to_profile(self):
        return self.find_clickable_element(ProfilePageLocators.PROFILE_BUTTON).click()

    @allure.step('Переход в Историю заказов')
    def click_to_order_history(self):
        return self.find_clickable_element(ProfilePageLocators.ORDERS_HISTORY_SECTION).click()

    @allure.step('Выход из аккаунта на странице профиля')
    def click_logout_link(self):
        return self.find_clickable_element(ProfilePageLocators.LOGOUT_LINK).click()

    @allure.step('Получить номер заказа в Истории заказов')
    def get_order_number(self):
        return self.get_current_text(ProfilePageLocators.ORDER_NUMBER_IN_PROFILE)

    @allure.step('Подождать загрузку заказов в профиле')
    def wait_for_order_number(self):
        return self.find_visible_element_located(ProfilePageLocators.ORDER_NUMBER_IN_PROFILE)

    @allure.step('Заполнить поле email')
    def fill_email(self, email):
        return self.find_visible_element_located(ProfilePageLocators.EMAIL_INPUT_FIELD).send_keys(email)

    @allure.step('Заполнить поле password')
    def fill_password(self, password):
        return self.find_visible_element_located(ProfilePageLocators.PASSWORD_INPUT_FIELD).send_keys(password)

    @allure.step('Нажать на кнопку Войти в аккаунт')
    def click_login_button(self):
        return self.find_clickable_element(ProfilePageLocators.LOGIN_BUTTON).click()

    @allure.step('Подождать загрузку раздела профиля пользователя')
    def wait_for_profile_section(self):
        return self.find_visible_element_located(ProfilePageLocators.PROFILE_SECTION)

    @allure.step('Подождать загрузку страницы авторизации')
    def wait_for_login_page(self):
        return self.find_visible_element_located(ProfilePageLocators.LOGIN_BUTTON)

    @allure.step('Получить текст кнопки авторизации')
    def get_login_button_text(self):
        return self.get_current_text(ProfilePageLocators.LOGIN_BUTTON)
