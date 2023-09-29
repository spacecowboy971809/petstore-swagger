from pet_requests import *
from src.assertions import *
import allure


# Define a test case for finding pets by a status not in the enum
@allure.epic("Pets_tests")
def test_find_by_status_not_in_enum():
    """
    Test find pets by status not in enum
    Parameters:
    status *: array[string]
    (query)
    Status values that need to be considered for filter
    Available values : available, pending, sold
    """
    # Specify a status that is not in the enum
    status = "test"

    # Try finding pets by the specified status
    find_by_status_response = find_by_status(status)

    # Assert that the response status code is 400 (Bad Request)
    assert find_by_status_response.status_code == 400, "Wrong response code for find by status response"

    # Assert that the response message indicates an invalid status value
    Assertions.assert_json_value(find_by_status_response, "message", "Invalid status value",
                                 "Wrong message find by status response")
