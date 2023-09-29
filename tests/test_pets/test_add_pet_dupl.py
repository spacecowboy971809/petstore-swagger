import pytest
from pet_requests import *
from src.test_data import *
import allure


# Define a test case for adding a duplicate pet
@pytest.mark.parametrize("api_key", [APIKeys.VALID_API_KEY.value])
@pytest.mark.parametrize("payload", [PetPayloads.CAT.value])
@allure.epic("Pets_tests")
def test_add_pet_dupl(payload, api_key):
    """
    Add existing pet to the store
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
    # Check if a pet with the given ID exists, and add it if it doesn't
    find_by_pet_id_response = find_by_pet_id(pet_id=payload ["id"])
    if find_by_pet_id_response.status_code != 200:
        response_add = add_pet(pet_id=payload ["id"],
                               category=payload ["category"],
                               name=payload ["name"],
                               photo_urls=payload ["photoUrls"],
                               tags=payload ["tags"],
                               status=payload ["status"])
        assert response_add.status_code == 200, "Wrong response code for add pet"

    # Add the same pet again and check that it fails (response status code != 200)
    response = add_pet(pet_id=payload ["id"],
                       category=payload ["category"],
                       name=payload ["name"],
                       photo_urls=payload ["photoUrls"],
                       tags=payload ["tags"],
                       status=payload ["status"])
    assert response.status_code != 200, "Wrong response code for adding a duplicate pet"
