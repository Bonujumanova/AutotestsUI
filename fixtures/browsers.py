from typing import Any, Generator
import pytest
from playwright.sync_api import sync_playwright, Page, Playwright


@pytest.fixture
def firefox_page(playwright: Playwright) -> Generator[Page, Any, None]:
    browser = playwright.firefox.launch(headless=False)
    yield browser.new_page()
    browser.close()


@pytest.fixture(scope="session")
def initialize_browser_state(playwright: Playwright):
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
    context.storage_state(path="browser-state.json")
    browser.close()


@pytest.fixture(scope="function")
def firefox_page_with_state(initialize_browser_state, playwright: Playwright) -> Generator[Page, Any, None]:
    browser = playwright.chromium.launch(headless=False)
    # Достает данные логин и пароль из хранилища
    context = browser.new_context(storage_state="browser-state.json")
    yield context.new_page()
    browser.close()
