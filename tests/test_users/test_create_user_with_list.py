import pytest
from users_requests import *
from src.test_data import *
from src.assertions import *
import allure


@pytest.mark.parametrize("payload", [UserPayloads.USER.value])
@pytest.mark.parametrize("payload_2", [UserPayloads.USER_2.value])
@allure.epic("Users_tests")
def test_create_user_with_list(payload, payload_2):
    """
    Test function create user with list
    body *: object
    (body)
        [User{
        id:	integer($int64)
        username: string
        firstName: string
        lastName: string
        email: string
        password: string
        phone: string
        userStatus:	integer($int32)
        }]
    """
    # Check if the first user exists and delete if necessary
    find_user_response = get_user_by_username(username=payload ["username"])
    if find_user_response.status_code == 200:
        delete_user_response = delete_user_by_username(username=payload ["username"])
        assert delete_user_response.status_code == 200, "Wrong response code for delete user"

    # Check if the second user exists and delete if necessary
    find_user_response = get_user_by_username(username=payload_2 ["username"])
    if find_user_response.status_code == 200:
        delete_user_response = delete_user_by_username(username=payload_2 ["username"])
        assert delete_user_response.status_code == 200, "Wrong response code for delete user"

    # Create the first user
    create_user_response = create_user_with_list(
        id=payload ["id"],
        username=payload ["username"],
        first_name=payload ["first_name"],
        last_name=payload ["last_name"],
        email=payload ["email"],
        password=payload ["password"],
        phone=payload ["phone"],
        user_status=payload ["user_status"],
        id_2=payload_2 ["id"],
        username_2=payload_2 ["username"],
        first_name_2=payload_2 ["first_name"],
        last_name_2=payload_2 ["last_name"],
        email_2=payload_2 ["email"],
        password_2=payload_2 ["password"],
        phone_2=payload_2 ["phone"],
        user_status_2=payload_2 ["user_status"]
    )
    assert create_user_response.status_code == 200, "Wrong response code for create user with list"

    # Verify attributes of the first user
    find_user_response = get_user_by_username(username=payload ["username"])
    assert find_user_response.status_code == 200, "Wrong response code for get user by username"
    Assertions.assert_json_value(find_user_response, "id", payload ["id"], "Id does not match")
    Assertions.assert_json_value(find_user_response, "username", payload ["username"], "Username does not match")
    # Add more assertions for other attributes if needed

    # Verify attributes of the second user
    find_user_response = get_user_by_username(username=payload_2 ["username"])
    assert find_user_response.status_code == 200, "Wrong response code for get user by username"
    Assertions.assert_json_value(find_user_response, "id", payload_2 ["id"], "Id does not match")
    Assertions.assert_json_value(find_user_response, "username", payload_2 ["username"], "Username does not match")
    # Add more assertions for other attributes if needed

    # Delete the first user
    delete_user_response = delete_user_by_username(username=payload ["username"])
    assert delete_user_response.status_code == 200, "Wrong response code for delete user"

    # Delete the second user
    delete_user_response = delete_user_by_username(username=payload_2 ["username"])
    assert delete_user_response.status_code == 200, "Wrong response code for delete user"
