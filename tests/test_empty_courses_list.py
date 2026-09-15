import pytest
from playwright.sync_api import sync_playwright, expect, Page

from pages.courses_list_page import CourseListPage


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(courses_list_page: CourseListPage):
    # Открытие страницы с автоматической авторизацией
    courses_list_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")
    courses_list_page.navbar.check_visible("username")
    courses_list_page.sidebar.check_visible()

    # Проверка отображения заголовка
    courses_list_page.check_visible_courses_title()

    # Проверка отображения кнопки Создать курс
    courses_list_page.check_visible_create_course_button()

    # Проверка отображения пустого блока с текстом "There is no results"
    courses_list_page.check_visible_empty_view()






    # # Проверка наличия текста заголовка "Courses"
    # courses_header = courses_list_page.get_by_test_id("courses-list-toolbar-title-text")
    # expect(courses_header).to_be_visible()
    # expect(courses_header).to_have_text("Courses")
    #
    # # Проверка наличия пустой иконки
    # icon_locator = courses_list_page.get_by_test_id("courses-list-empty-view-icon")
    # expect(icon_locator).to_be_visible()
    #
    # # Проверка наличия текста 'There is no results'
    # no_results_text_locator = courses_list_page.get_by_test_id("courses-list-empty-view-title-text")
    # expect(no_results_text_locator).to_be_visible()
    # expect(no_results_text_locator).to_have_text("There is no results")
    #
    # # Проверка наличия блока 'Results from the load test pipeline will be displayed here'
    # results_text_locator = courses_list_page.get_by_test_id("courses-list-empty-view-description-text")
    # expect(results_text_locator).to_be_visible()
    # expect(results_text_locator).to_have_text("Results from the load test pipeline will be displayed here")
    #
    # courses_list_page.wait_for_timeout(5000)