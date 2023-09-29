import pytest
from users_requests import *
from src.test_data import *
import allure


@pytest.mark.parametrize("payload", [UserPayloads.USER.value])
@pytest.mark.parametrize("payload_2", [UserPayloads.USER_2.value])
@allure.epic("Users_tests")
def test_create_user_with_list_dupl(payload, payload_2):
    """
    Test function create user with list duplicate
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
    # Check if the first user exists, and create if not
    get_user_response = get_user_by_username(username=payload ["username"])
    if get_user_response.status_code != 200:
        create_user_response = create_user(
            id=payload ["id"],
            username=payload ["username"],
            first_name=payload ["first_name"],
            last_name=payload ["last_name"],
            email=payload ["email"],
            password=payload ["password"],
            phone=payload ["phone"],
            user_status=payload ["user_status"]
        )
        assert create_user_response.status_code == 200, "Wrong response code for create user"

    # Check if the second user exists, and create if not
    get_user_response = get_user_by_username(username=payload ["username"])
    if get_user_response.status_code != 200:
        create_user_response = create_user(
            id=payload_2 ["id"],
            username=payload_2 ["username"],
            first_name=payload_2 ["first_name"],
            last_name=payload_2 ["last_name"],
            email=payload_2 ["email"],
            password=payload_2 ["password"],
            phone=payload_2 ["phone"],
            user_status=payload_2 ["user_status"]
        )
        assert create_user_response.status_code == 200, "Wrong response code for create user"

    # Attempt to create users with a list, expecting a bad response code
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

    # Assert that the create user request should not return a 200 status code for bad types
    assert create_user_response.status_code != 200, "Wrong response code for create user"
