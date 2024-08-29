from selenium.webdriver.common.by import By


class OrdersFeedLocators:
    TOTAL_ORDERS_COUNT = (By.XPATH, '//p[text()="Выполнено за все время:"]/following-sibling::p[contains(@class,"digits-large")]')  # Количество  заказов за все время
    TODAY_ORDERS_COUNT = (By.XPATH, '//p[text()="Выполнено за сегодня:"]/following-sibling::p[contains(@class,"digits-large")]')  # Количество  заказов за сегодня
    READY_ORDERS_TEXT = (By.XPATH, '//li[text()="Все текущие заказы готовы!"]')  # Напдись "Все теущие заказы готовы"
    COUNTER_TOTAL_ORDERS = [By.XPATH, '//p[text()="Выполнено за все время:"]/following-sibling::p']  # Счетчик заказов за все время
    COUNTER_TODAY_ORDERS = [By.XPATH, '//p[text()="Выполнено за сегодня:"]/following-sibling::p']  # Счетчик заказов за сегодня
    ORDER_FEED_TITLE = By.XPATH, '//h1[text()="Лента заказов"]'  # Заголовок Лента заказов
    ORDER_CARD = (By.XPATH, '//li[contains(@class, "OrderHistory_listItem")]')  # Карточка Заказа
    ORDER_NUMBER_IN_FEED = By.XPATH, '//p[text()="{}"]'  # Номер заказа из Ленты заказов
    ORDER_NUMBER_IN_PROGRESS = (By.XPATH, '//*[contains(@class,"orderListReady")]//li[contains(@class,"digits-default")]')  # Номер заказа в работе
    ORDER_DETAILS_IN_POPUP = (By.XPATH, '//p[text()="Cостав"]')  # Надпись "Состав" в попапе деталей заказа
