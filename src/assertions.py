from requests import Response
import json


class Assertions:
    @staticmethod
    def assert_json_value(response: Response, name, expected_value, error_message):
        try:
            # Attempt to parse the response content as JSON
            response_json = response.json( )
        except json.JSONDecodeError:
            # Handle the case where the response content is not valid JSON
            assert False, f"Response does not contain JSON. Response text is '{response.text}'"

        # Check if the specified 'name' exists in the response JSON
        assert name in response_json, f"Response JSON doesn't have key '{name}'"

        # Compare the value associated with 'name' to the expected value
        assert response_json.get(name) == expected_value, error_message
