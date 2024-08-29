from selenium.webdriver.common.by import By


class PasswordRecoveryLocators:
    RESTORE_PASSWRD_LINK = (By.XPATH, '//a[@href = "/forgot-password"]')  # Ссылка для восстановления пароля
    EMAIL_INPUT_FIELD = (By.XPATH, '//label[text()="Email"]/following-sibling::input')  # Поле ввода почты
    RECOVERY_PASSWRD_BUTTON = (By.XPATH, '//button[text()="Восстановить"]')  # Кнопка Восстановить на странице Восстановления пароля
    PASSWORD_INPUT_FIELD = (By.XPATH, '//input[@type="password"]')  # Поле ввода  пароля на странице Восстановления пароля
    SAVE_BUTTON = (By.XPATH, '//button[text()="Сохранить"]')  # Кнопка Сохранить на странице Восстановления пароля
    SHOW_PASSWORD_BUTTON = (By.XPATH, '//div[contains(@class,"icon-action")]')  # Кнопка "показать/скрыть пароль"
    ACTIVE_PASSWORD_INPUT_FIELD = (By.XPATH, '//label[text()="Пароль"]/parent::div[contains(@class, "input_status_active")]')  # Активное поля ввода пароля
