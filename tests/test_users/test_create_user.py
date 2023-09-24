import pytest
from json.decoder import JSONDecodeError
from users_requests import *
from src.test_data import *
from src.assertions import *
import allure


# Test case for creating a user
@pytest.mark.parametrize("payload", [UserPayloads.USER.value])
@allure.epic("Users_tests")
@allure.description("Test function create user")
def test_create_user(payload):
    # Check if a user with the given username exists and delete it if not
    get_user_response = get_user_by_username(username=payload ["username"])
    if get_user_response.status_code == 200:
        delete_user_response = delete_user_by_username(username=payload ["username"])
        assert delete_user_response.status_code == 200, "Wrong response code for delete user"

    # Create the user
    create_user_response = create_user(id=payload ["id"],
                                       username=payload ["username"],
                                       first_name=payload ["first_name"],
                                       last_name=payload ["last_name"],
                                       email=payload ["email"],
                                       password=payload ["password"],
                                       phone=payload ["phone"],
                                       user_status=payload ["user_status"])
    assert create_user_response.status_code == 200, "Wrong response code for create user"

    # Parse the response
    try:
        parsed_response_text = create_user_response.json( )
    except JSONDecodeError:
        print("Response does not contain JSON")

    # Check if the response message matches the user ID
    assert parsed_response_text ["message"] == str(payload ["id"]), "Id does not match"

    # Get the user by username and assert the values
    get_user_response = get_user_by_username(username=payload ["username"])
    assert get_user_response.status_code == 200, "Wrong response code for get user by username"
    Assertions.assert_json_value(get_user_response, "id", payload ["id"], "Id does not match")
    Assertions.assert_json_value(get_user_response, "username", payload ["username"], "Username does not match")
    Assertions.assert_json_value(get_user_response, "firstName", payload ["first_name"], "First name does not match")
    Assertions.assert_json_value(get_user_response, "lastName", payload ["last_name"], "Last name does not match")
    Assertions.assert_json_value(get_user_response, "email", payload ["email"], "Email does not match")
    Assertions.assert_json_value(get_user_response, "password", payload ["password"], "Password does not match")
    Assertions.assert_json_value(get_user_response, "phone", payload ["phone"], "Phone does not match")
    Assertions.assert_json_value(get_user_response, "userStatus", payload ["user_status"], "User status does not match")

    # Delete the created user
    delete_user_response = delete_user_by_username(username=payload ["username"])
    assert delete_user_response.status_code == 200, "Wrong response code for delete user"
