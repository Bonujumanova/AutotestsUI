import pytest

@pytest.fixture
def clear_database():
    print("[FIXTURE] Удаление всех данных из базы данных")

@pytest.fixture()
def fill_books_database():
    print("[FIXTURE] Создание новых данных в базе данных")

@pytest.mark.usefixtures("clear_database")
def test_read_all_books_in_library():
    print("Reading all books")

@pytest.mark.usefixtures(
    "clear_database",
    "fill_books_database"
)
class TestLibrary:
    def read_book_from_library(self):
        ...

    def test_delete_book_from_library(self):
        ...