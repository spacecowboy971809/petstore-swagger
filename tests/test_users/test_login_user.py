import pytest
from users_requests import *
from src.test_data import *
import allure


@pytest.mark.parametrize("payload", [UserPayloads.USER.value])
@allure.epic("Users_tests")
@allure.description("Test function login user")
def test_login_user(payload):
    # Check if the user exists, and create if it doesn't
    get_user_response = get_user_by_username(username=payload ["username"])
    if get_user_response.status_code != 200:
        create_user_response = create_user(id=payload ["id"],
                                           username=payload ["username"],
                                           first_name=payload ["first_name"],
                                           last_name=payload ["last_name"],
                                           email=payload ["email"],
                                           password=payload ["password"],
                                           phone=payload ["phone"],
                                           user_status=payload ["user_status"])
        assert create_user_response.status_code == 200, "Wrong response code for create user"

    # Attempt to login with user credentials
    login_user_response = login_user(username=payload ["username"], password=payload ["password"])

    # Verify that the login is successful (status code is 200)
    assert login_user_response.status_code == 200, "Wrong response code for login user"

    # Verify that cookies are not empty
    assert login_user_response.cookies, "Cookies are empty"

    # Cleanup: delete the created user
    delete_user_response = delete_user_by_username(username=payload ["username"])
    assert delete_user_response.status_code == 200, "Wrong response code for delete user"
