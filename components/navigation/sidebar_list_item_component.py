from re import Pattern
from playwright.sync_api import Page, expect
from components.base_component import BaseComponent

# Исполняющий файл, содержит все методы для исполнения(выполнения)
# Отвечает за один атомарный компонент на странице
class SidebarListItemComponent(BaseComponent):
    def __init__(self, page: Page, identifier):
        super().__init__(page)

        # {identifier} - переменная, которая содержит название компонента, нужная для составления локатора
        # Иконка элемента
        self.icon = page.get_by_test_id(f"{identifier}-drawer-list-item-icon")
        # Заголовок элемента
        self.title = page.get_by_test_id(f"{identifier}-drawer-list-item-title-text")
        # Полностью элемент(включая иконку и заголовок)
        self.button = page.get_by_test_id(f"{identifier}-drawer-list-item-button")


    # Проверяет отображение компоненты элемента
    def check_visible(self, title: str):
        expect(self.icon).to_be_visible()

        expect(self.title).to_be_visible()
        expect(self.title).to_have_text(title)

        expect(self.button).to_be_visible()

    # Нажимает на кнопку и перенаправляет на другую страницу. Происходит проверка URL
    def navigate(self, expected_url: Pattern[str]):
        self.button.click()
        # check_current_url - метод из BaseComponent(базового класса)
        self.check_current_url(expected_url)


