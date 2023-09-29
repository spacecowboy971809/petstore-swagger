import pytest
from store_requests import *
from pet_requests import *
from src.test_data import *
from src.assertions import *
import allure


# Test case for placing an order
@pytest.mark.parametrize("payload", [PetPayloads.DOG.value])
@pytest.mark.parametrize("api_key", [APIKeys.VALID_API_KEY.value])
@pytest.mark.parametrize("order_payload", [OrderPayloads.ORDER_PLACED.value, OrderPayloads.ORDER_APPROVED.value,
                                           OrderPayloads.ORDER_DELIVERED.value])
@allure.epic("Store_tests")
def test_place_order(payload, order_payload, api_key):
    """
    Test place order
    body *: object
    (body)
        Order{
        id: integer($int64)
        petId: integer($int64)
        quantity: integer($int32)
        shipDate: string($date-time)
        status: string
        Enum:
        [ placed, approved, delivered ]
        complete: boolean
        }
    """
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

    # Find the placed order by ID
    find_by_id_response = find_purchase_by_id(order_id=order_payload ["id"])
    assert find_by_id_response.status_code == 200, "Wrong response code for find order by id"

    # Validate the order details
    Assertions.assert_json_value(find_by_id_response, "id", order_payload ["id"], "Order id does not match")
    Assertions.assert_json_value(find_by_id_response, "petId", order_payload ["petId"], "Pet id does not match")
    Assertions.assert_json_value(find_by_id_response, "quantity", order_payload ["quantity"], "Quantity does not match")
    Assertions.assert_json_value(find_by_id_response, "shipDate", order_payload ["shipDate"] + "+0000",
                                 "Ship date does not match")
    Assertions.assert_json_value(find_by_id_response, "status", order_payload ["status"], "Status date does not match")
    Assertions.assert_json_value(find_by_id_response, "complete", order_payload ["complete"],
                                 "Complete date does not match")

    # Delete the placed order
    delete_order_response = delete_purchase_by_id(order_id=order_payload ["id"])
    assert delete_order_response.status_code == 200, "Wrong response code for delete order"

    # Delete the pet used in the test
    delete_pet_response = delete_pet(pet_id=payload ["id"], api_key=api_key)
    assert delete_pet_response.status_code == 200, "Wrong response code for delete pet"
