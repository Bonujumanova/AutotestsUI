from playwright.sync_api import sync_playwright, expect, Page
import pytest
from pages.login_page import LoginPage


@pytest.mark.regression
@pytest.mark.authorization
# Перебор паролей и логинов
# @pytest.mark.parametrize("email", ["user.name@gmail.com", "user.name@gmail.com", "  "])
# @pytest.mark.parametrize("password", ["password", "  ", "password"])

# ВВод Логи пароль, которые хранятся в кортеже
@pytest.mark.parametrize("email, password",
                         [
                             ("user.name@gmail.com", "password"),
                             ("user.name@gmail.com", "  "),
                             ("  ", "password")

                         ])
def test_wrong_email_or_password_authorization(login_page: LoginPage, email: str, password: str):
    login_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
    login_page.fill_login_form(email=email, password=password)
    login_page.click_login_button()
    login_page.check_visible_wrong_email_or_password_alert()
