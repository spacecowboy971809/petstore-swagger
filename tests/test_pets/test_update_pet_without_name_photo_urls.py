import pytest
from pet_requests import *
from src.test_data import *
import allure


# Test case for updating a pet without name and photo URLs
@pytest.mark.parametrize("api_key", [APIKeys.VALID_API_KEY.value])
@pytest.mark.parametrize("payload", [PetPayloads.EMPTY_NAME.value, PetPayloads.NULL_PAYLOAD.value])
@pytest.mark.parametrize("payload_2", [PetPayloads.DOG.value])
@allure.epic("Pets_tests")
def test_update_pet_without_name_photo_urls(payload, payload_2, api_key):
    """
    Test update pet without name photo urls
    body *: object:
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
    # Check if a pet with the given ID exists
    find_by_pet_id_response = find_by_pet_id(pet_id=payload_2 ["id"])

    if find_by_pet_id_response.status_code == 200:
        # Delete the pet if it exists
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

    # Update the pet without name and photo URLs
    update_response = update_pet(pet_id=payload_2 ["id"],
                                 category=payload ["category"],
                                 name=payload ["name"],
                                 photo_urls=payload ["photoUrls"],
                                 tags=payload ["tags"],
                                 status=payload ["status"])

    # Assert that the update operation did not succeed
    assert update_response.status_code != 200, "Wrong response code for add pet"

    # Delete the pet
    delete_pet_response = delete_pet(pet_id=payload_2 ["id"], api_key=api_key)
    assert delete_pet_response.status_code == 200, "Wrong response code for delete pet"
