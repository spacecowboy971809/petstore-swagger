import pytest
from pet_requests import *
from src.test_data import *
from src.assertions import *
import allure


# Define a test case for adding a pet
@pytest.mark.parametrize("api_key", [APIKeys.VALID_API_KEY.value])
@pytest.mark.parametrize("payload", [PetPayloads.CAT.value, PetPayloads.DOG.value, PetPayloads.RACCOON.value])
@allure.epic("Pets_tests")
def test_add_pet(payload, api_key):
    """
    Add a new pet to the store
    body *:object:
    (body)
        Pet{
        id: integer($int64)
        Category:
        {id: integer($int64)
        name: string}
        name*: string
        photoUrls*: string
        tags:
        {id: integer($int64)
        name: string}
        status:	string
        pet status in the store
        Enum: [ available, pending, sold ]
        }
    """
    # Check if a pet with the given ID exists, and delete it if it does
    find_by_pet_id_response = find_by_pet_id(pet_id=payload ["id"])
    if find_by_pet_id_response.status_code == 200:
        delete_pet(pet_id=payload ["id"], api_key=api_key)

    # Add a new pet
    response = add_pet(pet_id=payload ["id"],
                       category=payload ["category"],
                       name=payload ["name"],
                       photo_urls=payload ["photoUrls"],
                       tags=payload ["tags"],
                       status=payload ["status"])

    # Check if the response status code is correct
    assert response.status_code == 200, "Wrong response code for add pet"

    # Check specific values in the response JSON
    if payload ["id"]:
        Assertions.assert_json_value(response, "id", payload ["id"], "Wrong pet_id in response")
    Assertions.assert_json_value(response, "category", payload ["category"], "Wrong category in response")
    Assertions.assert_json_value(response, "name", payload ["name"], "Wrong name in response")
    Assertions.assert_json_value(response, "photoUrls", payload ["photoUrls"], "Wrong photo_urls in response")
    Assertions.assert_json_value(response, "tags", payload ["tags"], "Wrong tags in response")
    Assertions.assert_json_value(response, "status", payload ["status"], "Wrong status in response")

    # Parse the response text to get the pet ID, and then delete the pet
    parsed_response_text = response.json( )
    delete_pet_response = delete_pet(pet_id=parsed_response_text.get("id"), api_key=api_key)

    # Check if the response code for deleting the pet is correct
    assert delete_pet_response.status_code == 200, "Wrong response code for delete pet"
