import pytest
from users_requests import *
from src.test_data import *
from src.assertions import *
import allure

@pytest.mark.parametrize("payload", [UserPayloads.USER.value])
@allure.epic("Users_tests")
@allure.description("Test get user by username")
def test_get_user_by_username(payload):
    # Check if the user exists, and delete if it does (cleanup)
    get_user_response = get_user_by_username(username=payload["username"])
    if get_user_response.status_code == 200:
        delete_user_response = delete_user_by_username(username=payload["username"])
        assert delete_user_response.status_code == 200, "Wrong response code for delete user"

    # Create the user
    create_user_response = create_user(
        id=payload["id"],
        username=payload["username"],
        first_name=payload["first_name"],
        last_name=payload["last_name"],
        email=payload["email"],
        password=payload["password"],
        phone=payload["phone"],
        user_status=payload["user_status"]
    )
    assert create_user_response.status_code == 200, "Wrong response code for create user"

    # Get the user by username
    get_user_response = get_user_by_username(username=payload["username"])
    assert get_user_response.status_code == 200, "Wrong response code for get user by username"

    # Perform assertions to verify user data
    Assertions.assert_json_value(get_user_response, "id", payload["id"], "Id does not match")
    Assertions.assert_json_value(get_user_response, "username", payload["username"], "Username does not match")
    Assertions.assert_json_value(get_user_response, "firstName", payload["first_name"], "First name does not match")
    Assertions.assert_json_value(get_user_response, "lastName", payload["last_name"], "Last name does not match")
    Assertions.assert_json_value(get_user_response, "email", payload["email"], "Email does not match")
    Assertions.assert_json_value(get_user_response, "password", payload["password"], "Password does not match")
    Assertions.assert_json_value(get_user_response, "phone", payload["phone"], "Phone does not match")
    Assertions.assert_json_value(get_user_response, "userStatus", payload["user_status"], "User status does not match")

    # Clean up: Delete the user
    delete_user_response = delete_user_by_username(username=payload["username"])
    assert delete_user_response.status_code == 200, "Wrong response code for delete user"

    # Verify that the user has been deleted (status code 404)
    get_user_response = get_user_by_username(username=payload["username"])
    assert get_user_response.status_code == 404, "Wrong response code for get user by username"
