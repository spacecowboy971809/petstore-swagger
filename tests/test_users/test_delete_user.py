import pytest
from users_requests import *
from src.test_data import *
import allure

@pytest.mark.parametrize("payload", [UserPayloads.USER.value])
@allure.epic("Users_tests")
@allure.description("Test function delete user")
def test_delete_user(payload):
    # Check if the user exists, and create if not
    get_user_response = get_user_by_username(username=payload["username"])
    if get_user_response.status_code != 200:
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

    # Delete the user
    delete_user_response = delete_user_by_username(username=payload["username"])
    assert delete_user_response.status_code == 200, "Wrong response code for delete user"

    # Verify that the user has been deleted (status code 404)
    get_user_response = get_user_by_username(username=payload["username"])
    assert get_user_response.status_code == 404, "Wrong response code for get user by username"

    # Attempt to delete the user again, expecting status code 404
    delete_user_response = delete_user_by_username(username=payload["username"])
    assert delete_user_response.status_code == 404, "Wrong response code for delete user"
