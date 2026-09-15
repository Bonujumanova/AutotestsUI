# UI-автотесты с использованием Playwright

Проект по автоматизации был создан с помощью **Python**, **Playwright**, **Pytest**.

Реализуется проверка интерфейса:
- Login page: регистрация / авторизация
- Dashboard page: Выводятся графики оценок, занятий, курсов студентов
- Courses page: Создание курса, добавление заданий
- Logout page: Выход из аккаунта


## 🛠 Используемые технологии

* **Python**
* **Playwright**
* **Pytest**
* **Page Object Model (POM)**
* **Pytest fixtures**
* **Git / GitHub**

## 🧪 Что реализовано

В проекте изучаются и применяются:

* автоматизация UI-тестов с помощью Playwright;
* взаимодействие с элементами страницы;
* работа с локаторами;
* проверки (`assertions`);
* Pytest fixtures;
* Page Object Model;
* организация тестов по файлам и директориям;
* создание переиспользуемых компонентов;
* запуск тестов через Pytest.

## ⚙️ Установка проекта

Для начала работы необходимо клонировать репозиторий:

```bash
>>> git clone https://github.com/Bonujumanova/AutotestsUI.git
>>> cd AutotestsUI
```

Создать виртуальное окружение:

```bash
python -m venv .venv
```

Активировать виртуальное окружение.

### Linux / macOS

```bash
source .venv/bin/activate
```

### Windows

```bash
.venv\Scripts\activate
```

Установить зависимости:

```bash
python -m pip install --upgrade pip
pip install pytest-playwright
```

Установить браузеры Playwright:

```bash
playwright install
```

## ▶️ Запуск тестов

Запустить все тесты:

```bash
pytest
```

Запустить тесты с подробным выводом:

```bash
pytest -v
```

Запустить конкретный тест:

```bash
pytest tests/test_example.py -v
```

