from pages.main_page import MainPage
from locators.order_feed_locators import OrdersFeedLocators
from locators.main_page_locators import MainPageLocators
from utils.expected_results import ExpectedResults
import allure


class TestMainOrderCreation:

    @allure.title('Проверка перехода в Конструктор')
    def test_transfer_to_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.click_go_to_profile()
        main_page.find_visible_element_located(MainPageLocators.CONSTRUCTOR_BUTTON)
        main_page.click_on_constructor_button()
        main_page.find_visible_element_located(MainPageLocators.CONSTRUCTOR_TITLE)
        assert main_page.get_current_text(MainPageLocators.CONSTRUCTOR_TITLE) == ExpectedResults.BUILD_BURGER

    @allure.title('Проверка перехода в Ленту заказов')
    def test_transfer_to_order_feed(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_order_list()
        main_page.find_visible_element_located(OrdersFeedLocators.ORDER_FEED_TITLE)
        assert main_page.get_current_text(OrdersFeedLocators.ORDER_FEED_TITLE) == ExpectedResults.ORDER_FEED

    @allure.title('Проверка появления всплывающего окна с деталями при клике на ингредиент')
    def test_popup_with_ingredient_details(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_ingredient()
        assert main_page.find_element_located(MainPageLocators.INGREDIENT_POPUP).is_displayed()

    @allure.title('Проверка закрытия всплывающего окна с деталями ингредиента')
    def test_popup_ingredient_closed(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_ingredient()
        main_page.find_visible_element_located(MainPageLocators.INGREDIENT_POPUP)
        main_page.close_popup_button()
        main_page.find_invisible_element_located(MainPageLocators.INGREDIENT_POPUP)
        assert not main_page.find_element_located(MainPageLocators.INGREDIENT_POPUP).is_displayed()

    @allure.title('Проверка изменения каунтера ингредиента')
    def test_ingredient_counter(self, driver):
        main_page = MainPage(driver)
        prev_counter = int(main_page.check_ingredient_counter())
        main_page.add_ingredient_in_order()
        now_counter = int(main_page.check_ingredient_counter())
        assert now_counter > prev_counter

    @allure.title('Проверка успешного создания заказа авторизованным пользователем')
    def test_authorized_user_make_order(self, driver, login):
        main_page = MainPage(driver)
        main_page.find_visible_element_located(MainPageLocators.INGREDIENT)
        main_page.add_ingredient_in_order()
        main_page.click_make_order()
        main_page.find_visible_element_located(MainPageLocators.ORDER_NUMBER)
        assert main_page.find_element_located(MainPageLocators.ORDER_ID).is_displayed()
