import pytest
from users_requests import *
from src.test_data import *
import allure


@pytest.mark.parametrize("payload", [UserPayloads.USER.value])
@allure.epic("Users_tests")
def test_login_bad_user(payload):
    """
    Test login bad user
    Parameters:
    username *: string
    (query)
    password *: string
    (query)
    """
    # Check if the user exists, and delete if it does (cleanup)
    get_user_response = get_user_by_username(username=payload ["username"])
    if get_user_response.status_code == 200:
        delete_user_response = delete_user_by_username(username=payload ["username"])
        assert delete_user_response.status_code == 200, "Wrong response code for delete user"

    # Attempt to login with bad user credentials
    login_user_response = login_user(username=payload ["username"], password=payload ["password"])

    # Verify that the login attempt fails (status code is not 200)
    assert login_user_response.status_code != 200, "Wrong response code for login bad user"
