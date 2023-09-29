import pytest
from pet_requests import *
from src.test_data import *
import allure


# Define a test case for finding a pet by ID with bad ID types
@pytest.mark.parametrize("payload", [PetPayloads.NULL_PAYLOAD.value, PetPayloads.INVALID_PET_ID.value])
@allure.epic("Pets_tests")
def test_find_by_pet_id_bad_id_types(payload):
    """
    Test find by pet id with bad id types
    Parameters:
    petId *: integer($int64)
    (path)
    """
    # Attempt to find a pet by an invalid or null ID and assert the response code
    find_by_pet_id_response = find_by_pet_id(pet_id=payload["id"])
    assert find_by_pet_id_response.status_code == 400, "Wrong response code for find pet by id"
