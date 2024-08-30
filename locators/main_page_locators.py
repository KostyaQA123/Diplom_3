from selenium.webdriver.common.by import By


class MainPageLocators:
    AUTH_BUTTON = (By.XPATH, '//button[text()="Войти в аккаунт"]')  # Кнопка "Войти в аккаунт" на главной
    PROFILE_BUTTON = (By.XPATH, '//p[text()="Личный Кабинет"]')  # Кнопка "Личный Кабинет"
    ORDER_FEED_BUTTON = (By.XPATH, '//p[text()="Лента Заказов"]/parent::a')  # Кнопка "Лента Заказов" в хэдере
    CONSTRUCTOR_BUTTON = (By.XPATH, '//p[text()="Конструктор"]/parent::a')  # Кнопка "Конструктор" в хэдере
    CONSTRUCTOR_TITLE = By.XPATH, '//h1[text()="Соберите бургер"]'  # Заголовок "Соберите бургер"
    INGREDIENT = (By.XPATH, '//*[@href="/ingredient/61c0c5a71d1f82001bdaaa6d"]')  # Ингредиент "Флюоресцентная булка R2-D3"
    INGREDIENT_POPUP = (By.XPATH, '//h2[text()="Детали ингредиента"]')  # Детали ингредиента
    CLOSE_POPUP_BUTTON = (By.XPATH, '//button[contains(@class, "Modal_modal__close_modified")]')  # Крестик закрытия всплывающего окна
    INGREDIENT_COUNTER = (By.XPATH, '//ul[1]/a[1]//p[contains(@class, "num")]')  # Счётчик ингредиента
    ORDER_BASKET = By.XPATH, '//ul[contains(@class,"basket")]'  # Корзина заказа
    MAKE_ORDER_BUTTON = By.XPATH, '//button[text()="Оформить заказ"]'  # Кнопка "Оформить заказ"
    ORDER_ID = (By.XPATH, '//p[text()="идентификатор заказа"]')  # Идентификатор заказа
    ORDER_FEED_TITLE = By.XPATH, '//h1[text()="Лента заказов"]'  # Заголовок Лента заказов
    ORDER_NUMBER = By.XPATH, '//*[contains(@class, "type_digits-large")]'  # Номер заказа в модальном окне
    DEFAULT_ORDER = By.XPATH, '//h2[text()="9999"]'  # Дефолтный номер заказа в попапе
    COVER_ELEMENT = (By.XPATH, "//*[contains(@class, 'Modal_modal__loading')]"
                               "/following::div[@class='Modal_modal_overlay__x2ZCr']")  # Перекрывающий элемент
