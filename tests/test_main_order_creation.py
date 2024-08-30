from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators
from utils.expected_results import ExpectedResults
import allure


class TestMainOrderCreation:

    @allure.title('Проверка перехода в Конструктор')
    def test_transfer_to_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.click_go_to_profile()
        main_page.click_on_constructor_button()
        main_page.wait_for_constructor_page()
        build_burger_text = main_page.get_constructor_header_text()
        assert build_burger_text == ExpectedResults.BUILD_BURGER

    @allure.title('Проверка перехода в Ленту заказов')
    def test_transfer_to_order_feed(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_order_list()
        main_page.wait_for_order_feed_page()
        order_feed_text = main_page.get_order_feed_header_text()
        assert order_feed_text == ExpectedResults.ORDER_FEED

    @allure.title('Проверка появления всплывающего окна с деталями при клике на ингредиент')
    def test_popup_with_ingredient_details(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_ingredient()
        assert main_page.find_element_located(MainPageLocators.INGREDIENT_POPUP).is_displayed()

    @allure.title('Проверка закрытия всплывающего окна с деталями ингредиента')
    def test_popup_ingredient_closed(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_ingredient()
        main_page.close_popup_button()
        invisible_ingredient_popup = main_page.wait_for_invisible_ingredient_details()
        assert not invisible_ingredient_popup.is_displayed()

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
        main_page.wait_for_visible_ingredient()
        main_page.add_ingredient_in_order()
        main_page.click_make_order()
        main_page.wait_for_order_number()
        order_id = main_page.wait_for_order_id()
        assert order_id.is_displayed()
