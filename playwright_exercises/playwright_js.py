from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.firefox.launch(headless=False)
    page = browser.new_page()
    # Ожидание загрузки страницы
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login",
                  wait_until = "networkidle")
    title_value: str = "Some Text"
    page.evaluate(
        """

        (text) => {
        
            const title = document.getElementById('authentication-ui-course-title-text');
            title.textContent = text
        }
        """, title_value
    )


    page.wait_for_timeout(5000)