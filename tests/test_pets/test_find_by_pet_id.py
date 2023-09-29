import pytest
from pet_requests import *
from src.test_data import *
from src.assertions import *
import allure


# Define a test case for finding a pet by ID
@pytest.mark.parametrize("api_key", [APIKeys.VALID_API_KEY.value])
@pytest.mark.parametrize("payload", [PetPayloads.DOG.value, PetPayloads.CAT.value])
@allure.epic("Pets_tests")
def test_find_by_pet_id(api_key, payload):
    """
    Test find by pet id
    Parameters:
    petId *: integer($int64)
    (path)
    """
    # Check if a pet with the given ID exists, and delete it if it does
    find_by_pet_id_response = find_by_pet_id(pet_id=payload ["id"])
    if find_by_pet_id_response.status_code == 200:
        delete_pet(pet_id=payload ["id"], api_key=api_key)

    # Add a new pet
    add_pet_response = add_pet(pet_id=payload ["id"],
                               category=payload ["category"],
                               name=payload ["name"],
                               photo_urls=payload ["photoUrls"],
                               tags=payload ["tags"],
                               status=payload ["status"])

    assert add_pet_response.status_code == 200, "Wrong response code for add pet"

    # Find the pet by its ID and assert the response data
    find_id_response = find_by_pet_id(pet_id=payload ["id"])
    assert find_id_response.status_code == 200, "Wrong response code for find pet by id"

    if payload ["id"]:
        Assertions.assert_json_value(find_id_response, "id", payload ["id"], "Wrong pet_id in response")

    Assertions.assert_json_value(find_id_response, "category", payload ["category"], "Wrong category in response")
    Assertions.assert_json_value(find_id_response, "name", payload ["name"], "Wrong name in response")
    Assertions.assert_json_value(find_id_response, "photoUrls", payload ["photoUrls"], "Wrong photo_urls in response")
    Assertions.assert_json_value(find_id_response, "tags", payload ["tags"], "Wrong tags in response")
    Assertions.assert_json_value(find_id_response, "status", payload ["status"], "Wrong status in response")

    # Delete the added pet and assert the response code
    parsed_response_text = find_id_response.json( )
    delete_pet_response = delete_pet(pet_id=parsed_response_text.get("id"), api_key=api_key)
    assert delete_pet_response.status_code == 200, "Wrong response code for delete pet"
