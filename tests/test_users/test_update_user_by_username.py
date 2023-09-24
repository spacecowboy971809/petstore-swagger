import pytest
from users_requests import *
from src.test_data import *
from src.assertions import *
import allure


@pytest.mark.parametrize("payload", [UserPayloads.USER.value])
@allure.epic("Users_tests")
@allure.description("Test function update user by username")
def test_update_user_by_username(payload):
    # Define new values for updating the user
    id_2 = 124141231
    first_name_2 = "test_user_2"
    last_name_2 = "test_last_name_2"
    email_2 = "test_email_2"
    password_2 = "test_password_2"
    phone_2 = "21748949124"
    user_status_2 = 1

    # Check if the user exists, and create if it doesn't
    get_user_response = get_user_by_username(username=payload ["username"])
    if get_user_response.status_code == 200:
        delete_user_response = delete_user_by_username(username=payload ["username"])
        assert delete_user_response.status_code == 200, "Wrong response code for delete user"

    # Create a new user
    create_user_response = create_user(id=payload ["id"],
                                       username=payload ["username"],
                                       first_name=payload ["first_name"],
                                       last_name=payload ["last_name"],
                                       email=payload ["email"],
                                       password=payload ["password"],
                                       phone=payload ["phone"],
                                       user_status=payload ["user_status"])

    # Verify that the user is created successfully
    assert create_user_response.status_code == 200, "Wrong response code for create user"

    # Update the user with new values
    update_user_response = update_user_by_username(id=id_2,
                                                   username=payload ["username"],
                                                   first_name=first_name_2,
                                                   last_name=last_name_2,
                                                   email=email_2,
                                                   password=password_2,
                                                   phone=phone_2,
                                                   user_status=user_status_2)

    # Verify that the user is updated successfully
    assert update_user_response.status_code == 200, "Wrong response code for update user"

    # Get the updated user and verify the updated values
    get_user_response = get_user_by_username(username=payload ["username"])
    assert get_user_response.status_code == 200, "Wrong response code for get user by username"
    Assertions.assert_json_value(get_user_response, "id", id_2, "Id does not match")
    Assertions.assert_json_value(get_user_response, "username", payload ["username"], "Username does not match")
    Assertions.assert_json_value(get_user_response, "firstName", first_name_2, "First name does not match")
    Assertions.assert_json_value(get_user_response, "lastName", last_name_2, "Last name does not match")
    Assertions.assert_json_value(get_user_response, "email", email_2, "Email does not match")
    Assertions.assert_json_value(get_user_response, "password", password_2, "Password does not match")
    Assertions.assert_json_value(get_user_response, "phone", phone_2, "Phone does not match")
    Assertions.assert_json_value(get_user_response, "userStatus", user_status_2, "User status does not match")

    # Cleanup: delete the created user
    delete_user_response = delete_user_by_username(username=payload ["username"])
    assert delete_user_response.status_code == 200, "Wrong response code for delete user"
