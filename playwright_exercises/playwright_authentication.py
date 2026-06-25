from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    # Сохранение локальных данных в хранилище
    context = browser.new_context()
    # Создание новой страницы
    page = context.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    email_field = page.get_by_test_id("registration-form-email-input").locator("input")
    email_value: str = "user.name@gmail.com"
    # Заполнение поля локатора
    email_field.fill(email_value)

    username_field = page.get_by_test_id("registration-form-username-input").locator("input")
    username_value: str = "username"
    # Заполнение поля локатора Username
    username_field.fill(username_value)

    password_fild = page.get_by_test_id("registration-form-password-input").locator("input")
    password_value: str = "password"
    # Заполнение локатора Password
    password_fild.fill(password_value)

    registration_button = page.get_by_test_id("registration-page-registration-button")
    registration_button.click()

    # Заполнение хранилища данными(login, password). browser-state.json - название файла
    context.storage_state(path="browser-state.json")

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="browser-state.json") # Указываем файл с сохраненным состоянием
    page = context.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard")

    page.wait_for_timeout(5000)

