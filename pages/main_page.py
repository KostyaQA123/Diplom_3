from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
import allure


class MainPage(BasePage):

    @allure.step('Переход в Конструктор')
    def click_on_constructor_button(self):
        return self.find_clickable_element(MainPageLocators.CONSTRUCTOR_BUTTON).click()

    @allure.step('Переход на страницу Лента заказов')
    def click_on_order_list(self):
        return self.find_clickable_element(MainPageLocators.ORDER_FEED_BUTTON).click()

    @allure.step('Кликнуть на ингредиент')
    def click_on_ingredient(self):
        return self.find_clickable_element(MainPageLocators.INGREDIENT).click()

    @allure.step('Подождать загрузку ингридиента')
    def wait_for_visible_ingredient(self):
        return self.find_visible_element_located(MainPageLocators.INGREDIENT)

    @allure.step('Переход на страницу профиля')
    def click_go_to_profile(self):
        return self.find_clickable_element(MainPageLocators.PROFILE_BUTTON).click()

    @allure.step('Закрыть попап кнопкой крестик')
    def close_popup_button(self):
        return self.find_clickable_element(MainPageLocators.CLOSE_POPUP_BUTTON).click()

    @allure.step('Добавить ингредиент в корзину заказа')
    def add_ingredient_in_order(self):
        return self.drag_and_drop_on_element(MainPageLocators.INGREDIENT, MainPageLocators.ORDER_BASKET)

    @allure.step('Получить количество доьавленного в корзину ингредиента')
    def check_ingredient_counter(self):
        return self.get_current_text(MainPageLocators.INGREDIENT_COUNTER)

    @allure.step('Нажать на кнопку Оформить заказ')
    def click_make_order(self):
        return self.find_clickable_element(MainPageLocators.MAKE_ORDER_BUTTON).click()

    @allure.step('Сохранить номер заказа')
    def receive_order_number(self):
        self.find_visible_element_located(MainPageLocators.ORDER_ID)
        self.find_visible_element_located(MainPageLocators.DEFAULT_ORDER)
        return self.get_current_text(MainPageLocators.ORDER_NUMBER)

    @allure.step('Закрыть попап заказа кнопкой крестик')
    def close_order_popup(self):
        self.find_invisible_element_located(MainPageLocators.COVER_ELEMENT)
        return self.find_clickable_element(MainPageLocators.CLOSE_POPUP_BUTTON).click()

    @allure.step('Подождать загрузку раздела Собери бургер')
    def wait_for_constructor_page(self):
        return self.find_visible_element_located(MainPageLocators.CONSTRUCTOR_TITLE)

    @allure.step('Получить текст заголовка Собери бургер')
    def get_constructor_header_text(self):
        return self.get_current_text(MainPageLocators.CONSTRUCTOR_TITLE)

    @allure.step('Подождать загрузку раздела Лента заказов')
    def wait_for_order_feed_page(self):
        return self.find_visible_element_located(MainPageLocators.ORDER_FEED_TITLE)

    @allure.step('Получить текст заголовка Лента заказов')
    def get_order_feed_header_text(self):
        return self.get_current_text(MainPageLocators.ORDER_FEED_TITLE)

    @allure.step('Подождать закрытие всплывающего окна с ингредиентами')
    def wait_for_invisible_ingredient_details(self):
        return self.find_invisible_element_located(MainPageLocators.INGREDIENT_POPUP)

    @allure.step('Подождать получение номера заказа')
    def wait_for_order_number(self):
        return self.find_visible_element_located(MainPageLocators.ORDER_NUMBER)

    @allure.step('Получить текст с номером заказа')
    def get_order_number_text(self):
        return self.get_current_text(MainPageLocators.ORDER_NUMBER)

    @allure.step('Подождать получение идентификатора заказа')
    def wait_for_order_id(self):
        return self.find_visible_element_located(MainPageLocators.ORDER_ID)
