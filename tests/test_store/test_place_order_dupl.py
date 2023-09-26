import pytest
from store_requests import *
from pet_requests import *
from src.test_data import *
from src.assertions import *
import allure


# Test case for placing an order
@pytest.mark.parametrize("payload", [PetPayloads.DOG.value])
@pytest.mark.parametrize("api_key", [APIKeys.VALID_API_KEY.value])
@pytest.mark.parametrize("order_payload", [OrderPayloads.ORDER_PLACED.value])
@allure.epic("Store_tests")
@allure.description("Test place order")
def test_place_order_dupl(payload, order_payload, api_key):
    # Check if a pet with the given ID exists and add it if not
    find_by_pet_id_response = find_by_pet_id(pet_id=payload ["id"])
    if find_by_pet_id_response.status_code != 200:
        response = add_pet(pet_id=payload ["id"],
                           category=payload ["category"],
                           name=payload ["name"],
                           photo_urls=payload ["photoUrls"],
                           tags=payload ["tags"],
                           status=payload ["status"])
        assert response.status_code == 200, "Wrong response code for add pet"

    # Check if an order with the given ID exists and delete it if not
    find_by_id_response = find_purchase_by_id(order_id=order_payload ["id"])
    if find_by_id_response.status_code == 200:
        delete_order_response = delete_purchase_by_id(order_id=order_payload ["id"])
        assert delete_order_response.status_code == 200, "Wrong response code for delete order"
    # Place the order
    place_order_response = place_order(order_id=order_payload ["id"],
                                       pet_id=order_payload ["petId"],
                                       quantity=order_payload ["quantity"],
                                       ship_date=order_payload ["shipDate"],
                                       status=order_payload ["status"],
                                       complete=order_payload ["complete"])
    assert place_order_response.status_code == 200, "Wrong response code for place order"

    # Place duplicate order
    place_order_response = place_order(order_id=order_payload ["id"],
                                       pet_id=order_payload ["petId"],
                                       quantity=order_payload ["quantity"],
                                       ship_date=order_payload ["shipDate"],
                                       status=order_payload ["status"],
                                       complete=order_payload ["complete"])
    assert place_order_response.status_code != 200, "Wrong response code for place order"
    # Delete the placed order
    delete_order_response = delete_purchase_by_id(order_id=order_payload ["id"])
    assert delete_order_response.status_code == 200, "Wrong response code for delete order"

    # Delete the pet used in the test
    delete_pet_response = delete_pet(pet_id=payload ["id"], api_key=api_key)
    assert delete_pet_response.status_code == 200, "Wrong response code for delete pet"
