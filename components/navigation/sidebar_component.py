import re
from components.base_component import BaseComponent
from playwright.sync_api import Page
from components.navigation.sidebar_list_item_component import SidebarListItemComponent

# Передает информацию другому классу, чтобы тот выполнил команды, которые были использованы в данном классе
# Данный класс ВЫЗЫВАЕТ методы из другого класса и передает различные аргументы.
# Получает компоненты страницы, происходит использование методов из Sidebar_list_item_component
class SidebarComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        # Передает переменную для поиска локатора
        self.logout_list_item = SidebarListItemComponent(page, "logout")
        self.courses_list_item = SidebarListItemComponent(page, "courses")
        self.dashboard_list_item = SidebarListItemComponent(page, "dashboard")

    def check_visible(self):
        self.logout_list_item.check_visible("Logout")

        self.courses_list_item.check_visible("Courses")

        self.dashboard_list_item.check_visible("Dashboard")



    def click_logout(self):
        # NAVIGATE() Нажимает на кнопку и перенаправляет на другую страницу. Происходит проверка URL
        self.logout_list_item.navigate(re.compile(r".*/#/auth/login"))

    def click_courses(self):
        # NAVIGATE() Нажимает на кнопку и перенаправляет на другую страницу. Происходит проверка URL
        self.logout_list_item.navigate(re.compile(r".*/#/courses"))

    def click_dashboard(self):
        # NAVIGATE() Нажимает на кнопку и перенаправляет на другую страницу. Происходит проверка URL
        self.dashboard_list_item.navigate(re.compile(r".*/#/dashboard"))





