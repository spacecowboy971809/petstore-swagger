import pytest
from pet_requests import *
from src.test_data import *
from src.assertions import *
import allure


# Define a test case for deleting a pet with bad types
@pytest.mark.parametrize("api_key", [APIKeys.VALID_API_KEY.value])
@allure.epic("Pets_tests")
@allure.description("Test delete pet")
def test_delete_pet_bad_types(api_key):
    delete_pet_response = delete_pet("test_string", api_key=api_key)

    # Assert error response
    assert delete_pet_response.status_code == 400, "Wrong response code for delete pet"
    Assertions.assert_json_value(delete_pet_response, "message", "Invalid ID supplied", "Wrong message delete Invalid ID supplied")
