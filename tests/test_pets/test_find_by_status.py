import pytest
from json.decoder import JSONDecodeError
from pet_requests import *
from src.test_data import *
import allure


# Define a test case for finding pets by status
@pytest.mark.parametrize("api_key", [APIKeys.VALID_API_KEY.value])
@pytest.mark.parametrize("payload", [PetPayloads.CAT.value])
@allure.epic("Pets_tests")
def test_find_by_status(payload, api_key):
    """
    Test find pets by status
    Parameters:
    status *: array[string]
    (query)
    Status values that need to be considered for filter
    Available values : available, pending, sold
    """
    # Check if a pet with the given ID exists and delete it if found
    find_by_pet_id_response = find_by_pet_id(pet_id=payload ["id"])
    if find_by_pet_id_response.status_code == 200:
        delete_pet_response = delete_pet(pet_id=payload ["id"], api_key=api_key)
        assert delete_pet_response.status_code == 200, "Wrong response code for delete pet"

    # Add a pet with the given payload
    response = add_pet(pet_id=payload ["id"],
                       category=payload ["category"],
                       name=payload ["name"],
                       photo_urls=payload ["photoUrls"],
                       tags=payload ["tags"],
                       status=payload ["status"])
    assert response.status_code == 200, "Wrong response code for add pet"

    # Find pets by status and assert that the added pet is found
    find_by_status_response = find_by_status(payload ["status"])
    assert find_by_status_response.status_code == 200, "Wrong response code for find by status"

    try:
        parsed_response_text = find_by_status_response.json( )
    except JSONDecodeError:
        print("Response does not contain JSON")

    # Find the added pet by ID in the response
    parsed_response_text = next((pet for pet in parsed_response_text if pet ['id'] == payload ["id"]), None)

    assert parsed_response_text, "Response does not contain added id"
    assert parsed_response_text.get("id") == payload ["id"], "Wrong pet_id in response"
    assert parsed_response_text.get("category") == payload ["category"], "Wrong category in response"
    assert parsed_response_text.get("name") == payload ["name"], "Wrong name in response"
    assert parsed_response_text.get("photoUrls") == payload ["photoUrls"], "Wrong photo_urls in response"
    assert parsed_response_text.get("tags") == payload ["tags"], "Wrong tags in response"
    assert parsed_response_text.get("status") == payload ["status"], "Wrong status in response"

    # Delete the added pet
    delete_pet_response = delete_pet(pet_id=parsed_response_text.get("id"), api_key=api_key)
    assert delete_pet_response.status_code == 200, "Wrong response code for delete pet"

    # Try finding the deleted pet by status and assert that it's not found
    find_by_status_response = find_by_status(payload ["status"])
    assert find_by_status_response.status_code == 200, "Wrong response code for find by status response"

    try:
        parsed_response_text = find_by_status_response.json( )
    except JSONDecodeError:
        print("Response does not contain JSON")

    parsed_response_text = next((pet for pet in parsed_response_text if pet ['id'] == payload ["id"]), None)
    assert parsed_response_text is None, "Response contains deleted id"
