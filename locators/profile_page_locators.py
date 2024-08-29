from selenium.webdriver.common.by import By


class ProfilePageLocators:
    ORDERS_HISTORY_SECTION = (By.XPATH, '//a[text()="История заказов"]')  # Заголовок История заказов
    LOGOUT_LINK = (By.XPATH, '//button[text() = "Выход"]')  # Ссылка для выхода из аккаунта
    EMAIL_INPUT_FIELD = (By.XPATH, '//label[text()="Email"]/following-sibling::input')  # Поле ввода почты для логина
    PASSWORD_INPUT_FIELD = (By.XPATH, '//label[text()="Пароль"]/following-sibling::input')  # Поле ввода пароля для логина
    LOGIN_BUTTON = (By.XPATH, '//button[contains(text(), "Войти")]')  # Кнопка Войти
    PROFILE_SECTION = (By.XPATH, '//a[text()="Профиль"]')  # Заголовок "Профиль" на странице личного кабинета
    ORDER_NUMBER_IN_PROFILE = (By.XPATH, '//*[contains(@class,"textBox")]//p[contains(@class,"digits-default")]') # Номер заказа в личном кабинете
