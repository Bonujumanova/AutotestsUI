import pytest

from pages.registration_page import RegistrationPage
from pages.dashboard_page import DashboardPage


# @pytest.mark.parametrize("email", "username", "password", ("user.name@gmail.com", "username", "password"))
@pytest.mark.regression
@pytest.mark.registration
def test_successful_registration(registration_page: RegistrationPage, dashboard_page: DashboardPage):

        registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
        email: str = "user.name@gmail.com"
        username: str = "username"
        password: str = "password"

        registration_page.fill_registration_form(email=email, username=username, password=password)
        registration_page.click_registration_button()

        dashboard_page.find_dashboard_title()










