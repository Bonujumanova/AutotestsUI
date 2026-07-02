import pytest
from playwright.sync_api import sync_playwright, expect, Page


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(firefox_page_with_state: Page):
    # Открытие страницы с автоматической авторизацией
    firefox_page_with_state.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    # Проверка наличия текста заголовка "Courses"
    courses_header = firefox_page_with_state.get_by_test_id("courses-list-toolbar-title-text")
    expect(courses_header).to_have_text("Courses")

    # Проверка наличия пустой иконки
    icon_locator = firefox_page_with_state.get_by_test_id("courses-list-empty-view-icon")
    expect(icon_locator).to_be_visible()

    # Проверка наличия текста 'There is no results'
    no_results_text_locator = firefox_page_with_state.get_by_test_id("courses-list-empty-view-title-text")
    expect(no_results_text_locator).to_be_visible()
    expect(no_results_text_locator).to_have_text("There is no results")

    # Проверка наличия блока 'Results from the load test pipeline will be displayed here'
    results_text_locator = firefox_page_with_state.get_by_test_id("courses-list-empty-view-description-text")
    expect(results_text_locator).to_be_visible()
    expect(results_text_locator).to_have_text("Results from the load test pipeline will be displayed here")

    firefox_page_with_state.wait_for_timeout(5000)