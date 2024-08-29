from pages.order_feed_page import OrderFeed
from locators.order_feed_locators import OrdersFeedLocators
from locators.profile_page_locators import ProfilePageLocators
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage
from pages.profile_page import ProfilePage
import allure


class TestOrderFeed:

    # @allure.title('Проверка открытия всплывающего окна с деталями заказа')
    # def test_open_order_details_popup(self, driver):
    #     feed_page = OrderFeed(driver)
    #     feed_page.click_order_feed()
    #     feed_page.find_visible_element_located(OrdersFeedLocators.ORDER_FEED_TITLE)
    #     feed_page.click_order_details()
    #     feed_page.find_visible_element_located(OrdersFeedLocators.ORDER_DETAILS_IN_POPUP)
    #     assert feed_page.find_element_located(OrdersFeedLocators.ORDER_DETAILS_IN_POPUP).is_displayed()
    #
    # @allure.title('Проверка отображения созданного заказа на странице Профиля и в Ленте заказов')
    # def test_order_from_profile_present_in_order_feed(self, driver, login):
    #     main_page = MainPage(driver)
    #     main_page.find_visible_element_located(MainPageLocators.INGREDIENT)
    #     main_page.add_ingredient_in_order()
    #     main_page.click_make_order()
    #     main_page.find_visible_element_located(MainPageLocators.DEFAULT_ORDER)
    #     main_page.find_visible_element_located(MainPageLocators.ORDER_ID)
    #     main_page.close_order_popup()
    #     profile_page = ProfilePage(driver)
    #     profile_page.click_go_to_profile()
    #     profile_page.find_visible_element_located(ProfilePageLocators.PROFILE_SECTION)
    #     profile_page.click_to_order_history()
    #     profile_page.find_visible_element_located(ProfilePageLocators.ORDER_NUMBER_IN_PROFILE)
    #     order = profile_page.get_order_number()
    #     main_page.click_on_order_list()
    #     feed_page = OrderFeed(driver)
    #     feed_page.find_visible_element_located(OrdersFeedLocators.ORDER_FEED_TITLE)
    #     order_in_list = feed_page.find_order_number(order)
    #     assert order in order_in_list
    #
    # @allure.title('Проверка увеличения счетчика Выполнено за всё время при создании нового заказа')
    # def test_total_order_counter_increase(self, driver, login):
    #     main_page = MainPage(driver)
    #     feed_page = OrderFeed(driver)
    #     main_page.click_on_order_list()
    #     feed_page.find_visible_element_located(OrdersFeedLocators.ORDER_FEED_TITLE)
    #     current_orders_count = feed_page.get_total_orders()
    #     main_page.click_on_constructor_button()
    #     main_page.find_visible_element_located(MainPageLocators.CONSTRUCTOR_TITLE)
    #     main_page.add_ingredient_in_order()
    #     main_page.click_make_order()
    #     main_page.find_visible_element_located(MainPageLocators.DEFAULT_ORDER)
    #     main_page.find_visible_element_located(MainPageLocators.ORDER_ID)
    #     main_page.close_order_popup()
    #     main_page.click_on_order_list()
    #     main_page.find_visible_element_located(OrdersFeedLocators.ORDER_FEED_TITLE)
    #     increased_orders_count = feed_page.get_total_orders()
    #     assert increased_orders_count > current_orders_count
    #
    # @allure.title('Проверка увеличения счетчика Выполнено за сегодня при создании нового заказа')
    # def test_today_order_counter_increase(self, driver, login):
    #     main_page = MainPage(driver)
    #     feed_page = OrderFeed(driver)
    #     main_page.click_on_order_list()
    #     feed_page.find_visible_element_located(OrdersFeedLocators.ORDER_FEED_TITLE)
    #     current_orders_count = feed_page.get_today_orders()
    #     main_page.click_on_constructor_button()
    #     main_page.find_visible_element_located(MainPageLocators.CONSTRUCTOR_TITLE)
    #     main_page.add_ingredient_in_order()
    #     main_page.click_make_order()
    #     main_page.find_visible_element_located(MainPageLocators.DEFAULT_ORDER)
    #     main_page.find_visible_element_located(MainPageLocators.ORDER_ID)
    #     main_page.close_order_popup()
    #     main_page.click_on_order_list()
    #     main_page.find_visible_element_located(OrdersFeedLocators.ORDER_FEED_TITLE)
    #     increased_orders_count = feed_page.get_today_orders()
    #     assert increased_orders_count > current_orders_count

    @allure.title('Проверка появления номера заказа в разделе В работе после его оформления')
    def test_order_in_progress_after_checkout(self, driver, login):
        main_page = MainPage(driver)
        feed_page = OrderFeed(driver)
        main_page.find_visible_element_located(MainPageLocators.CONSTRUCTOR_TITLE)
        main_page.add_ingredient_in_order()
        main_page.click_make_order()
        main_page.find_invisible_element_located(MainPageLocators.DEFAULT_ORDER)
        main_page.find_visible_element_located(MainPageLocators.ORDER_ID)
        my_order = main_page.get_current_text(MainPageLocators.ORDER_NUMBER)
        main_page.close_order_popup()
        main_page.click_on_order_list()
        orders_in_progress = feed_page.get_order_number_in_progress()
        assert my_order in orders_in_progress
