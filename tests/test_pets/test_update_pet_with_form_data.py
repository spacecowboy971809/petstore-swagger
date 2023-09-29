import pytest
from pet_requests import *
from src.test_data import *
from src.assertions import *
import allure


# Test case for updating a pet with form data
@pytest.mark.parametrize("api_key", [APIKeys.VALID_API_KEY.value])
@pytest.mark.parametrize("payload", [PetPayloads.DOG.value])
@allure.epic("Pets_tests")
def test_update_pet_with_form_data(payload, api_key):
    """
    Test update pet with form data
    Parameters:
    petId *: integer($int64)
    (path)
    name: string
    (formData)
    status: string
    (formData)
    """
    # New values for name and status
    name_2 = "test12442424"
    status_2 = "sold"

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
    assert update_with_form_data_response.status_code == 200, "Wrong response code for update pet with form data"

    # Find the updated pet by ID
    find_id_response = find_by_pet_id(pet_id=payload ["id"])
    assert find_id_response.status_code == 200, "Wrong response code for find pet by id"

    # Assert that the updated pet information matches the expected values
    if payload ["id"]:
        Assertions.assert_json_value(find_id_response, "id", payload ["id"], "Wrong pet_id in response")
    Assertions.assert_json_value(find_id_response, "category", payload ["category"], "Wrong category in response")
    Assertions.assert_json_value(find_id_response, "name", name_2, "Wrong name in response")
    Assertions.assert_json_value(find_id_response, "photoUrls", payload ["photoUrls"], "Wrong photo_urls in response")
    Assertions.assert_json_value(find_id_response, "tags", payload ["tags"], "Wrong tags in response")
    Assertions.assert_json_value(find_id_response, "status", status_2, "Wrong status in response")

    # Delete the updated pet
    parsed_response_text = find_id_response.json( )
    delete_pet_response = delete_pet(pet_id=parsed_response_text.get("id"), api_key=api_key)
    assert delete_pet_response.status_code == 200, "Wrong response code for delete pet"

    # Update deleted pet  using form data
    update_with_form_data_response = update_pet_with_form(pet_id=payload ["id"], name=name_2, status=status_2)
    assert update_with_form_data_response.status_code != 200, "Wrong response code for update pet with form data"
