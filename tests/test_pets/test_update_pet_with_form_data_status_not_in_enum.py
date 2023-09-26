import pytest
from pet_requests import *
from src.test_data import *
import allure


# Test case for updating a pet with form data
@pytest.mark.parametrize("api_key", [APIKeys.VALID_API_KEY.value])
@pytest.mark.parametrize("payload", [PetPayloads.DOG.value])
@allure.epic("Pets_tests")
@allure.description("Test update pet with form data")
def test_update_pet_with_form_data_status_not_in_enum(payload, api_key):
    # New values for name and status
    name_2 = "test12442424"
    status_2 = "test"

    # Check if a pet with the given ID exists
    find_by_id_response = find_by_pet_id(pet_id=payload ["id"])

    if find_by_id_response.status_code != 200:
        # Add a new pet if it doesn't exist
        add_pet_response = add_pet(pet_id=payload ["id"],
                                   category=payload ["category"],
                                   name=payload ["name"],
                                   photo_urls=payload ["photoUrls"],
                                   tags=payload ["tags"],
                                   status=payload ["status"])
        assert add_pet_response.status_code == 200, "Wrong response code for add pet"

    # Update the pet using form data
    update_with_form_data_response = update_pet_with_form(pet_id=payload ["id"], name=name_2, status=status_2)
    assert update_with_form_data_response.status_code != 200, "Wrong response code for update pet with form data with status not in enum"
