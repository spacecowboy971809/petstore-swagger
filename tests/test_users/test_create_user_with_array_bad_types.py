import pytest
from users_requests import *
from src.test_data import *
import allure


# Test case for creating users with an array of data with bad types
@pytest.mark.parametrize("payload", [UserPayloads.USER_BAD_ID.value])
@pytest.mark.parametrize("payload_2", [UserPayloads.USER_BAD_STATUS.value])
@allure.epic("Users_tests")
def test_create_user_with_array_bad_types(payload, payload_2):
    """
    Test function create user with array bad types
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
    # Check if the first user with the given username exists and delete it if found
    get_user_response = get_user_by_username(username=payload ["username"])
    if get_user_response.status_code == 200:
        delete_user_response = delete_user_by_username(username=payload ["username"])
        assert delete_user_response.status_code == 200, "Wrong response code for delete user"

    # Check if the second user with the given username exists and delete it if found
    get_user_response = get_user_by_username(username=payload_2 ["username"])
    if get_user_response.status_code == 200:
        delete_user_response = delete_user_by_username(username=payload_2 ["username"])
        assert delete_user_response.status_code == 200, "Wrong response code for delete user"

    # Attempt to create users with the provided data, which has bad types
    create_user_response = create_user_with_array(
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

    # Check if user creation with bad types failed (should not return 200 status code)
    assert create_user_response.status_code != 200, "Wrong response code for create user"
