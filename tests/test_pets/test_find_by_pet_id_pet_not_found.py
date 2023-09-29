import pytest
from pet_requests import *
from src.test_data import *
from src.assertions import *
import allure


# Define a test case for finding a pet by ID when the pet is not found
@pytest.mark.parametrize("api_key", [APIKeys.VALID_API_KEY.value])
@pytest.mark.parametrize("payload", [PetPayloads.DOG.value])
@allure.epic("Pets_tests")
def test_find_by_pet_id_pet_not_found(payload, api_key):
    """
    Test find by pet id, pet not found
    Parameters:
    petId *: integer($int64)
    (path)
    """
    # Check if a pet with the given ID exists and delete it if found
    find_by_pet_id_response = find_by_pet_id(pet_id=payload ["id"])
    if find_by_pet_id_response.status_code == 200:
        delete_pet(pet_id=payload ["id"], api_key=api_key)

    # Attempt to find a pet by ID and assert that it's not found
    find_id_response = find_by_pet_id(pet_id=payload ["id"])
    assert find_id_response.status_code == 404, "Wrong response code for find pet by id"
    Assertions.assert_json_value(find_id_response, "message", "Pet not found", "Wrong message find by status response")
