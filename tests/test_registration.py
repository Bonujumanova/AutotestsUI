from playwright.sync_api import sync_playwright, expect, Page
import pytest

@pytest.mark.registration
@pytest.mark.regression
@pytest.mark.usefixtures("firefox_page_with_state")
def test_successful_registration(firefox_page: Page ):

        firefox_page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

        email_field = firefox_page.get_by_test_id("registration-form-email-input").locator("input")
        email_value: str = "user.name@gmail.com"
        # Заполнение поля локатора
        email_field.fill(email_value)

        username_field = firefox_page.get_by_test_id("registration-form-username-input").locator("input")
        username_value: str = "username"
        # Заполнение поля локатора Username
        username_field.fill(username_value)

        password_fild = firefox_page.get_by_test_id("registration-form-password-input").locator("input")
        password_value: str = "password"
        # Заполнение локатора Password
        password_fild.fill(password_value)

        registration_button = firefox_page.get_by_test_id("registration-page-registration-button")
        registration_button.click()

        dashboard_title = firefox_page.get_by_test_id("dashboard-drawer-list-item-title-text")
        expect(dashboard_title).to_be_visible()

        firefox_page.wait_for_timeout(5000)







