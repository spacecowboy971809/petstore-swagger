import pytest
from store_requests import *
from src.test_data import *
import allure


# Test case for deleting an order
@pytest.mark.parametrize("payload", [PetPayloads.DOG.value])
@pytest.mark.parametrize("api_key", [APIKeys.VALID_API_KEY.value])
@pytest.mark.parametrize("order_payload", [OrderPayloads.ORDER_PLACED.value])
@allure.epic("Store_tests")
@allure.description("Test delete order")
def test_delete_order(payload, order_payload, api_key):
    # Check if the order with the given ID exists
    find_by_id_response = find_purchase_by_id(order_id=order_payload ["id"])

    if find_by_id_response.status_code != 200:
        # Place the order if it doesn't exist
        place_order_response = place_order(order_id=order_payload ["id"],
                                           pet_id=order_payload ["petId"],
                                           quantity=order_payload ["quantity"],
                                           ship_date=order_payload ["shipDate"],
                                           status=order_payload ["status"],
                                           complete=order_payload ["complete"])
        assert place_order_response.status_code == 200, "Wrong response code for place order"

    # Delete the order
    delete_order_response = delete_purchase_by_id(order_id=order_payload ["id"])

    # Assert that the order has been deleted successfully
    assert delete_order_response.status_code == 200, "Wrong response code for delete order"

    # Attempt to delete the order again
    delete_order_response = delete_purchase_by_id(order_id=order_payload ["id"])

    # Assert that the order is not found (404 status)
    assert delete_order_response.status_code == 404, "Wrong response code for delete order"
