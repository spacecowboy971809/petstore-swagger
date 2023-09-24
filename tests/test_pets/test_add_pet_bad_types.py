import pytest
from json.decoder import JSONDecodeError
from pet_requests import *
from src.test_data import *
import allure


# Define a test case for adding a pet with bad types
@pytest.mark.parametrize("api_key", [APIKeys.VALID_API_KEY.value])
@pytest.mark.parametrize("payload", [PetPayloads.NULL_PAYLOAD.value, PetPayloads.INVALID_ID.value,
                                     PetPayloads.INVALID_CATEGORY_ID.value, PetPayloads.INVALID_CATEGORY_NAME.value])
@allure.epic("Pets_tests")
@allure.description("Test add pet with bad types")
def test_add_pet_bad_types(payload, api_key):
    # Check if a pet with the given ID exists, and delete it if it does
    find_by_pet_id_response = find_by_pet_id(pet_id=payload ["id"])
    if find_by_pet_id_response.status_code == 200:
        delete_pet(pet_id=payload ["id"], api_key=api_key)

    # Add a new pet with payload containing bad types and check the response
    response = add_pet(pet_id=payload ["id"],
                       category=payload ["category"],
                       name=payload ["name"],
                       photo_urls=payload ["photoUrls"],
                       tags=payload ["tags"],
                       status=payload ["status"])

    # Check if the response error code is correct (405 - Invalid input)
    assert response.status_code == 405, "Wrong response error code for add pet with bad types"
