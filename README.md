# Дипломный проект. Задание 3: Web-тесты

### Автотесты для проверки программы, которая помогает заказать бургер в Stellar Burgers

Основа для написания автотестов — фреймворк pytest и selenium

## Реализованные сценарии

### TestPasswordRecovery
* test_click_recovery_link_on_main_page — Проверка перехода на страницу восстановления пароля по кнопке Восстановить пароль
* test_fill_email_click_recovery — Проверка ввода почты и клик по кнопке Восстановить
* test_password_field_highlight_on_switch_visibility — Проверка подсветки активного поля ввода пароля при клике на показать/скрыть пароль

### TestProfile
* test_transfer_to_profile_page — Проверка перехода по клику в Личный кабинет
* test_transfer_to_order_history — Проверка перехода в раздел История заказов на странице профиля
* test_user_logout — Проверка выхода из аккаунта

### TestMainOrderCreation
* test_transfer_to_constructor — Проверка перехода в Конструктор
* test_transfer_to_order_feed — Проверка перехода в Ленту заказов
* test_popup_with_ingredient_details — Проверка появления всплывающего окна с деталями при клике на ингредиент
* test_popup_ingredient_closed — Проверка закрытия всплывающего окна с деталями ингредиента
* test_ingredient_counter — Проверка изменения каунтера ингредиента
* test_authorized_user_make_order — Проверка успешного создания заказа авторизованным пользователем

### TestOrderFeed
* test_open_order_details_popup — Проверка открытия всплывающего окна с деталями заказа
* test_order_from_profile_present_in_order_feed — Проверка отображения созданного заказа на странице Профиля и в Ленте заказов
* test_total_order_counter_increase — Проверка увеличения счетчика Выполнено за всё время при создании нового заказа
* test_today_order_counter_increase — Проверка увеличения счетчика Выполнено за сегодня при создании нового заказа
* test_order_in_progress_after_checkout — Проверка появления номера заказа в разделе В работе после его оформления

## Запуск автотестов

**Установка зависимостей**

> `$ pip install -r requirements.txt`

**Запуск автотестов и создание Allure-отчета**

>  `pytest -v tests/ --alluredir=allure_results`

**Посмотреть отчёт о тестировании**

>  `allure serve allure_results`