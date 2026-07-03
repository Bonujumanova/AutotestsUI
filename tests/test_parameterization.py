import pytest
from _pytest.fixtures import SubRequest

@pytest.mark.parametrize("number", [1, 2, 3, -1])
def test_numbers(number):
    # assert number > 0
    ...

@pytest.mark.parametrize("number, expected", [(1, 1), (2, 4), (3, 9)])
def test_several_numbers(number, expected):
    assert 1 ** 2 == 1

def test_several_numbers_2():
    assert 2 ** 2 == 4

def test_several_numbers_3():
    assert 3 ** 2 == 9

@pytest.fixture(params=["chromium", "webkit", "firefox"])
def browser(request):
    return request.param

def test_open_browser(browser: str):
    print(f"Running test on browser: {browser}")


@pytest.mark.parametrize("user", ["Alice", "Zara"])
class TestOperations:
    @pytest.mark.parametrize("account", ["Credit Card", "Debit Card"])
    def test_user_with_operations(self,user: str,  account: str):
        print(f"User with operations: {user}")

    def test_user_without_operations(self, user: str):
        print(f"User without operations: {user}")


users = {"+799999": "User with money on bank account",
         "+788888": "User without money on bank account",
         "+744444": "User with operations on bank account"
}
@pytest.mark.parametrize("phone_number",
                         users.keys(),
                         ids=lambda phone_number: f"{phone_number}: {users[phone_number]}"
)
def test_identifiers(phone_number: str):
    ...