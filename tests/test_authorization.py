from playwright.sync_api import sync_playwright, expect
import pytest

@pytest.mark.regression
@pytest.mark.authorization
def test_wrong_email_or_password_authorization():
    with sync_playwright() as playwright:
        firefox = playwright.chromium.launch(headless=False)
        page = firefox.new_page()
        # открываем страницу
        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
        # находим локатор
        # email_input = page.locator('//div[@data-testid="login-form-email-input"]//div//input')
        # Также можно искать локатор через test-id
        email_input = page.get_by_test_id("login-form-email-input").locator("input")
        # заполняем поле локатора
        email_input.fill('user.name@gmail.com')

        # Ищем локатор поля пароль
        password_input = page.locator('//div[@data-testid="login-form-password-input"]//div//input')
        # Заполняем поле локатора пароль
        password_input.fill("Password")

        # Ищем локатор кнопки button
        # login_button = page.locator('//button[@data-testid="login-page-login-button"]')
        # Также можно искать локатор через test-id
        login_button = page.get_by_test_id("login-page-login-button")
        # Нажимаем на кнопку Login
        login_button.click()

        # Локатор всплывающего окна "Wrong email or password"
        wrong_email_or_password_alert = page.locator('//div[@data-testid="login-page-wrong-email-or-password-alert"]')

        # Проверяем, что данный локатор видимый
        expect(wrong_email_or_password_alert).to_be_visible()
        # Проверка, что локатор содержит определенный текст
        expect(wrong_email_or_password_alert).to_have_text("Wrong email or password")

        # Ожидание, задерживает страницу на виду в течение выставленного времени
        # 5000 - 5 secund

        page.wait_for_timeout(5000)


