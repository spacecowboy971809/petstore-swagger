from store_requests import *
from src.assertions import *
import allure


# Test case for deleting an order with bad types
@allure.epic("Store_tests")
def test_delete_order_bad_types():
    """
    Test delete order with bad type orderId
    Parameters:
    orderId *: integer($int64)
    (path)
    """
    # Delete the order with bad types
    delete_order_response = delete_purchase_by_id("test_string")

    # Assert error response
    assert delete_order_response.status_code == 400, "Wrong response code for delete pet"
    Assertions.assert_json_value(delete_order_response, "message", "Invalid ID supplied", "Wrong message delete invalid ID supplied")
