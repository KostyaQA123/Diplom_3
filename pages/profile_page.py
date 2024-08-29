from pages.base_page import BasePage
from locators.profile_page_locators import ProfilePageLocators
from locators.main_page_locators import MainPageLocators
import allure


class ProfilePage(BasePage):

    @allure.step('Переход на страницу профиля')
    def click_go_to_profile(self):
        return self.find_clickable_element(MainPageLocators.PROFILE_BUTTON).click()

    @allure.step('Переход в Историю заказов')
    def click_to_order_history(self):
        return self.find_clickable_element(ProfilePageLocators.ORDERS_HISTORY_SECTION).click()

    @allure.step('Выход из аккаунта на странице профиля')
    def click_logout_link(self):
        return self.find_clickable_element(ProfilePageLocators.LOGOUT_LINK).click()

    @allure.step('Получить номер заказа в Истории заказов')
    def get_order_number(self):
        return self.get_current_text(ProfilePageLocators.ORDER_NUMBER_IN_PROFILE)
