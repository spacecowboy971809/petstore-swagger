import pytest
from pet_requests import *
from src.test_data import *
from src.assertions import *
import allure


# Test case for updating a pet
@pytest.mark.parametrize("api_key", [APIKeys.VALID_API_KEY.value])
@pytest.mark.parametrize("payload", [PetPayloads.CAT.value])
@pytest.mark.parametrize("payload_2", [PetPayloads.DOG.value])
@allure.epic("Pets_tests")
@allure.description("Test update pet")
def test_update_pet(payload, payload_2, api_key):
    # Check if a pet with the given ID exists and delete it if found
    find_by_pet_id_response = find_by_pet_id(pet_id=payload_2 ["id"])
    if find_by_pet_id_response.status_code == 200:
        delete_pet_response = delete_pet(pet_id=payload_2 ["id"], api_key=api_key)
        assert delete_pet_response.status_code == 200, "Wrong response code for delete pet"

    # Add a new pet
    response = add_pet(pet_id=payload_2 ["id"],
                       category=payload_2 ["category"],
                       name=payload_2 ["name"],
                       photo_urls=payload_2 ["photoUrls"],
                       tags=payload_2 ["tags"],
                       status=payload_2 ["status"])
    assert response.status_code == 200, "Wrong response code for add pet"

    # Update the pet with new information
    update_response = update_pet(pet_id=payload_2 ["id"],
                                 category=payload ["category"],
                                 name=payload ["name"],
                                 photo_urls=payload ["photoUrls"],
                                 tags=payload ["tags"],
                                 status=payload ["status"])

    # Assert that the response status code indicates a successful update
    assert update_response.status_code == 200, "Wrong response code for update pet"

    # Check if the updated pet information matches the expected values
    if payload_2 ["id"]:
        Assertions.assert_json_value(update_response, "id", payload_2 ["id"], "Wrong pet_id in response")
    Assertions.assert_json_value(update_response, "category", payload ["category"], "Wrong category in response")
    Assertions.assert_json_value(update_response, "name", payload ["name"], "Wrong name in response")
    Assertions.assert_json_value(update_response, "photoUrls", payload ["photoUrls"], "Wrong photo_urls in response")
    Assertions.assert_json_value(update_response, "tags", payload ["tags"], "Wrong tags in response")
    Assertions.assert_json_value(update_response, "status", payload ["status"], "Wrong status in response")

    # Delete the updated pet
    parsed_response_text = update_response.json( )
    delete_pet_response = delete_pet(pet_id=parsed_response_text.get("id"), api_key=api_key)
    assert delete_pet_response.status_code == 200, "Wrong response code for delete pet"
