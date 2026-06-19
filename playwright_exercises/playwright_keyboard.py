from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.firefox.launch(headless=False)
    page = browser.new_page()
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    login_email_input = page.get_by_test_id('login-form-email-input').locator('input')
    # принудительно устанавливает фокус ввода на выбранный веб-элемент
    login_email_input.focus()

    # Вводит по одному элементу в поле
    for char in "user.name@gmail.com":
        page.keyboard.type(char, delay=100)
    # Выделяет полностью текст в поле
    page.keyboard.press("ControlOrMeta+A")



    page.wait_for_timeout(5000)