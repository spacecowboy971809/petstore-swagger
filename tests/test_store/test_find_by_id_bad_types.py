from store_requests import *
from src.assertions import *
import allure


# Test case for finding an order by ID
@allure.epic("Store_tests")
@allure.description("Test find order by id with bad types")
def test_find_by_id_bad_types():
    # Find the order by ID
    find_by_id_response = find_purchase_by_id('test_string')

    # Assert error response
    assert find_by_id_response.status_code == 400, "Wrong response code for delete pet"
    Assertions.assert_json_value(find_by_id_response, "message", "Invalid ID supplied", "Wrong message find by invalid ID supplied")
