import pytest
from playwright.sync_api import sync_playwright, expect

"""DON'T USE IT"""
@pytest.mark.courses
@pytest.mark.regression

def _dont_use_test_empty_courses_list():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        # Сохранение локальных данных в хранилище
        context = browser.new_context()
        # Открывает пустую вкладку
        page = context.new_page()
        # Переход браузера по указанной ссылке
        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

        # Поиск поля Email
        email_field = page.get_by_test_id("registration-form-email-input").locator("input")
        email_value: str = "user.name@gmail.com"
        # Заполнение поля локатора
        email_field.fill(email_value)

        # Поиск поля Username
        username_field = page.get_by_test_id("registration-form-username-input").locator("input")
        username_value: str = "username"
        # Заполнение поля локатора Username
        username_field.fill(username_value)

        # Поиск локатора Password
        password_fild = page.get_by_test_id("registration-form-password-input").locator("input")
        password_value: str = "password"
        # Заполнение локатора Password
        password_fild.fill(password_value)

        registration_button = page.get_by_test_id("registration-page-registration-button")
        registration_button.click()

        # Заполнение хранилища данными(login, password). browser-state2.json - название файла
        context.storage_state(path="browser-state2.json")

    # Открытие страницы с автоматической авторизацией
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        # Достает данные логин и пароль из хранилища
        context = browser.new_context(storage_state="browser-state2.json")
        page = context.new_page()
        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

        # Проверка наличия текста заголовка "Courses"
        courses_header = page.get_by_test_id("courses-list-toolbar-title-text")
        expect(courses_header).to_have_text("Courses")

        # Проверка наличия пустой иконки
        icon_locator = page.get_by_test_id("courses-list-empty-view-icon")
        expect(icon_locator).to_be_visible()

        # Проверка наличия текста 'There is no results'
        no_results_text_locator = page.get_by_test_id("courses-list-empty-view-title-text")
        expect(no_results_text_locator).to_be_visible()
        expect(no_results_text_locator).to_have_text("There is no results")

        # Проверка наличия блока 'Results from the load test pipeline will be displayed here'
        results_text_locator = page.get_by_test_id("courses-list-empty-view-description-text")
        expect(results_text_locator).to_be_visible()
        expect(results_text_locator).to_have_text("Results from the load test pipeline will be displayed here")

        page.wait_for_timeout(5000)
