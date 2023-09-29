import pytest
from pet_requests import *
from src.test_data import *
import allure


# Define a test case for deleting a pet without API keys
@pytest.mark.parametrize("payload", [PetPayloads.DOG.value])
@allure.epic("Pets_tests")
def test_delete_pet_no_api_key(payload):
    """
    Test delete pet with no api key
    Parameters:
    api_key:string
    (header)
    petId *: integer($int64)
    (path)
    """
    # Check if a pet with the given ID exists, and add it if it doesn't
    find_if_response = find_by_pet_id(pet_id=payload ["id"])
    if find_if_response.status_code != 200:
        # Add the pet
        add_pet_response = add_pet(pet_id=payload ["id"],
                                   category=payload ["category"],
                                   name=payload ["name"],
                                   photo_urls=payload ["photoUrls"],
                                   tags=payload ["tags"],
                                   status=payload ["status"])
        assert add_pet_response.status_code == 200, "Wrong response code for add pet"

    # Attempt to delete the pet without API keys and check that it fails (response status code is not 200)
    delete_pet_response = delete_pet_without_api_key(pet_id=payload ["id"])
    assert delete_pet_response.status_code != 200, "Wrong response code for delete pet without api_keys"
