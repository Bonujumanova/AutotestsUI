from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.firefox.launch(headless=False)
    page = browser.new_page()
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    # Поиск кнопки "Registration"
    registration_button = page.get_by_test_id("registration-page-registration-button")
    # Проверка, что кнопка недоступна
    expect(registration_button).to_be_disabled()

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
    # Проверка, что кнопка Registration стала доступна
    expect(registration_button).to_be_enabled()





    page.wait_for_timeout(5000)


    

