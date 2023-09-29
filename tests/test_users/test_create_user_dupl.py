import pytest
from users_requests import *
from src.test_data import *
import allure


# Test case for creating a duplicate user
@pytest.mark.parametrize("payload", [UserPayloads.USER.value])
@allure.epic("Users_tests")
def test_create_user_dupl(payload):
    """
    Test function create user duplicate
    body *: object
    (body)
        User{
        id:	integer($int64)
        username: string
        firstName: string
        lastName: string
        email: string
        password: string
        phone: string
        userStatus:	integer($int32)
        }
    """
    # Check if a user with the given username exists and create it if not
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

    # Attempt to create a duplicate user with the same username, expecting a non-200 status code
    create_user_response = create_user(id=payload ["id"],
                                       username=payload ["username"],
                                       first_name=payload ["first_name"],
                                       last_name=payload ["last_name"],
                                       email=payload ["email"],
                                       password=payload ["password"],
                                       phone=payload ["phone"],
                                       user_status=payload ["user_status"])
    assert create_user_response.status_code != 200, "Wrong response code for create duplicate user"

    # Clean up by deleting the created user
    delete_user_response = delete_user_by_username(username=payload ["username"])
    assert delete_user_response.status_code == 200, "Wrong response code for delete user"
