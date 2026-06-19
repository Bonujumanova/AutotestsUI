from playwright.sync_api import sync_playwright, expect


with sync_playwright() as playwright:

    firefox_browser = playwright.firefox.launch(headless=False)
    page = firefox_browser.new_page()
    # Открытие страницы по ссылке
    url_address: str = "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration"
    page.goto(url_address)

    # Заполнение поля email
    email_input = page.get_by_test_id("registration-form-email-input").locator("input")
    email_address_value: str = "user.name@gmail.com"
    email_input.fill(email_address_value)

    # Заполнение поля Username
    username = page.get_by_test_id("registration-form-username-input").locator("input")
    username_value: str = "username"
    username.fill(username_value)

    # Заполнение поля password
    password_input = page.get_by_test_id("registration-form-password-input").locator("input")
    password_value: str = "password"
    password_input.fill(password_value)

    # Кликание на кнопку Registration
    registration_button = page.get_by_test_id("registration-page-registration-button")
    registration_button.click()

    # Проверка наличия заголовка Dashboard
    dashboard_title = page.get_by_test_id("dashboard-toolbar-title-text")
    expect(dashboard_title).to_be_visible()
    expect(dashboard_title).to_have_text("Dashboard")







