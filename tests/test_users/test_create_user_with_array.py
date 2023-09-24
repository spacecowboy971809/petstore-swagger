import pytest
from users_requests import *
from src.test_data import *
from src.assertions import *
import allure

# Test case for creating users with an array of data
@pytest.mark.parametrize("payload", [UserPayloads.USER.value])
@pytest.mark.parametrize("payload_2", [UserPayloads.USER_2.value])
@allure.epic("Users_tests")
@allure.description("Test function create user with array")
def test_create_user_with_array(payload, payload_2):
    # Check if the first user with the given username exists and delete it if found
    get_user_response = get_user_by_username(username=payload["username"])
    if get_user_response.status_code == 200:
        delete_user_response = delete_user_by_username(username=payload["username"])
        assert delete_user_response.status_code == 200, "Wrong response code for delete user"

    # Check if the second user with the given username exists and delete it if found
    get_user_response = get_user_by_username(username=payload_2["username"])
    if get_user_response.status_code == 200:
        delete_user_response = delete_user_by_username(username=payload_2["username"])
        assert delete_user_response.status_code == 200, "Wrong response code for delete user"

    # Create users with the provided data from the payloads
    create_user_response = create_user_with_array(
        id=payload["id"],
        username=payload["username"],
        first_name=payload["first_name"],
        last_name=payload["last_name"],
        email=payload["email"],
        password=payload["password"],
        phone=payload["phone"],
        user_status=payload["user_status"],
        id_2=payload_2["id"],
        username_2=payload_2["username"],
        first_name_2=payload_2["first_name"],
        last_name_2=payload_2["last_name"],
        email_2=payload_2["email"],
        password_2=payload_2["password"],
        phone_2=payload_2["phone"],
        user_status_2=payload_2["user_status"]
    )

    # Check if user creation was successful
    assert create_user_response.status_code == 200, "Wrong response code for create user"

    # Check the first user's data
    get_user_response = get_user_by_username(username=payload["username"])
    assert get_user_response.status_code == 200, "Wrong response code for get user by username"
    Assertions.assert_json_value(get_user_response, "id", payload["id"], "Id does not match")
    Assertions.assert_json_value(get_user_response, "username", payload["username"], "Username does not match")
    Assertions.assert_json_value(get_user_response, "firstName", payload["first_name"], "First name does not match")
    Assertions.assert_json_value(get_user_response, "lastName", payload["last_name"], "Last name does not match")
    Assertions.assert_json_value(get_user_response, "email", payload["email"], "Email does not match")
    Assertions.assert_json_value(get_user_response, "password", payload["password"], "Password does not match")
    Assertions.assert_json_value(get_user_response, "phone", payload["phone"], "Phone does not match")
    Assertions.assert_json_value(get_user_response, "userStatus", payload["user_status"], "User status does not match")

    # Check the second user's data
    get_user_response = get_user_by_username(username=payload_2["username"])
    assert get_user_response.status_code == 200, "Wrong response code for get user by username"
    Assertions.assert_json_value(get_user_response, "id", payload_2["id"], "Id does not match")
    Assertions.assert_json_value(get_user_response, "username", payload_2["username"], "Username does not match")
    Assertions.assert_json_value(get_user_response, "firstName", payload_2["first_name"], "First name does not match")
    Assertions.assert_json_value(get_user_response, "lastName", payload_2["last_name"], "Last name does not match")
    Assertions.assert_json_value(get_user_response, "email", payload_2["email"], "Email does not match")
    Assertions.assert_json_value(get_user_response, "password", payload_2["password"], "Password does not match")
    Assertions.assert_json_value(get_user_response, "phone", payload_2["phone"], "Phone does not match")
    Assertions.assert_json_value(get_user_response, "userStatus", payload_2["user_status"], "User status does not match")

    # Clean up by deleting the created users
    delete_user_response = delete_user_by_username(username=payload["username"])
    assert delete_user_response.status_code == 200, "Wrong response code for delete user"
    delete_user_response = delete_user_by_username(username=payload_2["username"])
    assert delete_user_response.status_code == 200, "Wrong response code for delete user"
