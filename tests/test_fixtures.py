import pytest
from _pytest import fixtures


@pytest.fixture(autouse=True)
def send_analytics():
    print("[AUTO_USE] Отправление данных в сервис аналитики")

@pytest.fixture(scope="session")
def settings():
    print("[SESSION] Инициализация настроек автотестов")

@pytest.fixture(scope="class")
def user():
    print("[CLASS] создание данных пользователя один раз на тестовый класс")

@pytest.fixture(scope="function")
def browser():
    print("[FUNCTION] Открываем браузер на каждый автотест")


class TestUserFlow:
    def test_user_can_login(self, settings, user, browser):
        ...

    def test_user_can_course(self, settings, user, browser):
        ...

class TestAccountFlow:
    def test_user_account(self, settings, user, browser):
        ...