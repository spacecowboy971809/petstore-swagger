import pytest
from users_requests import *
from src.test_data import *
import allure

# Test case for creating a user with bad types
@pytest.mark.parametrize("payload", [UserPayloads.USER_BAD_ID.value, UserPayloads.USER_BAD_STATUS.value])
@allure.epic("Users_tests")
@allure.description("Test function create user with bad types")
def test_create_user_bad_types(payload):
    # Check if a user with the given username exists and delete it if not
    get_user_response = get_user_by_username(username=payload["username"])
    if get_user_response.status_code == 200:
        delete_user_response = delete_user_by_username(username=payload["username"])
        assert delete_user_response.status_code == 200, "Wrong response code for delete user"

    # Attempt to create a user with bad types, expecting a non-200 status code
    create_user_response = create_user(id=payload["id"],
                                       username=payload["username"],
                                       first_name=payload["first_name"],
                                       last_name=payload["last_name"],
                                       email=payload["email"],
                                       password=payload["password"],
                                       phone=payload["phone"],
                                       user_status=payload["user_status"])
    assert create_user_response.status_code != 200, "Wrong response code for create user with bad type"
