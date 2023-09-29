import pytest
from json.decoder import JSONDecodeError
from store_requests import *
from pet_requests import *
from src.test_data import *
from src.assertions import *
import allure


# Test case for checking inventory
@pytest.mark.parametrize("payload", [PetPayloads.CAT.value, PetPayloads.DOG.value, PetPayloads.RACCOON.value])
@pytest.mark.parametrize("api_key", [APIKeys.VALID_API_KEY.value])
@allure.epic("Store_tests")
def test_inventory(payload, api_key):
    """
    Test inventory
    Returns a map of status codes to quantities
    """
    # Check if a pet with the given ID exists and delete it
    find_by_pet_id_response = find_by_pet_id(pet_id=payload ["id"])
    if find_by_pet_id_response.status_code == 200:
        delete_pet(pet_id=payload ["id"], api_key=api_key)

    # Get the initial inventory status
    inventory_response = return_inventory( )
    assert inventory_response.status_code == 200, "Wrong response code for inventory"

    try:
        parsed_response_text = inventory_response.json( )
    except JSONDecodeError:
        print("Response does not contain JSON")

    # Get the initial count of pets with the specified status
    count = 0
    if parsed_response_text.get(payload ["status"]):
        count += parsed_response_text.get(payload ["status"], 0)

    # Add a pet with the specified status
    response = add_pet(pet_id=payload ["id"],
                       category=payload ["category"],
                       name=payload ["name"],
                       photo_urls=payload ["photoUrls"],
                       tags=payload ["tags"],
                       status=payload ["status"])

    assert response.status_code == 200, "Wrong response code for add pet"

    # Get the inventory status after adding the pet
    inventory_response = return_inventory( )
    assert inventory_response.status_code == 200, "Wrong response code for inventory"
    # Verify that the count of pets with the specified status has increased by 1
    Assertions.assert_json_value(inventory_response, payload ["status"], count + 1,
                                 "Wrong response count for inventory")

    # Delete the added pet
    delete_pet_response = delete_pet(pet_id=payload ["id"], api_key=api_key)
    assert delete_pet_response.status_code == 200, "Wrong response code for delete pet"

    # Get the inventory status after deleting the pet
    inventory_response = return_inventory( )
    assert inventory_response.status_code == 200, "Wrong response code for inventory"

    try:
        parsed_response_text = inventory_response.json( )
    except JSONDecodeError:
        print("Response does not contain JSON")

    if parsed_response_text.get(payload ["status"]):
        # Verify that the count of pets with the specified status has returned to its original value
        Assertions.assert_json_value(inventory_response, payload ["status"], count, "Wrong response count for inventory")
