from pages.base_page import BasePage
from locators.order_feed_locators import OrdersFeedLocators
from locators.main_page_locators import MainPageLocators
import allure


class OrderFeed(BasePage):

    @allure.step('Посмотреть детали заказа в списке Ленты заказов')
    def click_order_details(self):
        return self.find_clickable_element(OrdersFeedLocators.ORDER_CARD).click()

    @allure.step('Посмотреть детали заказа в списке Ленты заказов')
    def click_order_feed(self):
        return self.find_clickable_element(MainPageLocators.ORDER_FEED_BUTTON).click()

    @allure.step('Найти заказ по номеру в Ленте заказов')
    def find_order_number(self, order):
        path = OrdersFeedLocators.ORDER_NUMBER_IN_FEED[0]
        locator = OrdersFeedLocators.ORDER_NUMBER_IN_FEED[1]
        locator = locator.format(order)
        return self.get_current_text((path, locator))

    @allure.step('Найти заказ по номеру среди заказов в работе')
    def get_order_number_in_progress(self):
        self.find_visible_element_located(OrdersFeedLocators.READY_ORDERS_TEXT)
        self.find_invisible_element_located(OrdersFeedLocators.READY_ORDERS_TEXT)
        return self.get_current_text(OrdersFeedLocators.ORDER_NUMBER_IN_PROGRESS)

    @allure.step('Получить количество заказов, выполненных за всё время')
    def get_total_orders(self):
        return self.get_current_text(OrdersFeedLocators.TOTAL_ORDERS_COUNT)

    @allure.step('Получить количество заказов, выполненных за сегодня')
    def get_today_orders(self):
        return self.get_current_text(OrdersFeedLocators.TODAY_ORDERS_COUNT)