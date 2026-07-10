import pytest
from playwright.sync_api import Page

from fixtures.browsers import firefox_page_with_state
from pages.courses_list_page import CourseListPage
from pages.create_course_page import CreateCoursePage
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage

@pytest.fixture()
def login_page(firefox_page: Page) -> LoginPage:
    return LoginPage(page=firefox_page)

@pytest.fixture()
def registration_page(firefox_page: Page) -> RegistrationPage:
    return RegistrationPage(page=firefox_page)

@pytest.fixture()
def dashboard_page(firefox_page: Page) -> DashboardPage:
    return DashboardPage(page=firefox_page)

@pytest.fixture()
def courses_list_page(firefox_page_with_state: Page) -> CourseListPage:
    return CourseListPage(page=firefox_page_with_state)

@pytest.fixture()
def create_course_page(firefox_page_with_state: Page) -> CreateCoursePage:
    return CreateCoursePage(page=firefox_page_with_state)