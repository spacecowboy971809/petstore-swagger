import requests
from src.logger import Logger
import allure


class MyRequests:
    @staticmethod
    def get(url, json=None, headers=None, cookies=None, files=None):
        # Create an Allure step to log the GET request
        with allure.step(f"GET request to URL '{url}"):
            return MyRequests._send(url, json, headers, cookies, "GET", files)

    @staticmethod
    def post(url, json=None, headers=None, cookies=None, files=None):
        # Create an Allure step to log the POST request
        with allure.step(f"POST request to URL '{url}"):
            return MyRequests._send(url, json, headers, cookies, "POST", files)

    @staticmethod
    def put(url, json=None, headers=None, cookies=None, files=None):
        # Create an Allure step to log the PUT request
        with allure.step(f"PUT request to URL '{url}"):
            return MyRequests._send(url, json, headers, cookies, "PUT", files)

    @staticmethod
    def delete(url, json=None, headers=None, cookies=None, files=None):
        # Create an Allure step to log the DELETE request
        with allure.step(f"DELETE request to URL '{url}"):
            return MyRequests._send(url, json, headers, cookies, "DELETE", files)

    @staticmethod
    def _send(url, json, headers, cookies, method, files):
        # Construct the full URL
        url = f"https://petstore.swagger.io/v2/{url}"

        # Initialize headers and cookies if not provided
        if headers is None:
            headers = {}
        if cookies is None:
            cookies = {}

        # Log the request using the Logger class
        Logger.add_request(url, json, headers, cookies, method, files)

        # Send the HTTP request based on the specified method
        if method == "GET":
            response = requests.get(url, params=json, headers=headers, cookies=cookies, files=files)
        elif method == "POST":
            response = requests.post(url, json=json, headers=headers, cookies=cookies, files=files)
        elif method == "PUT":
            response = requests.put(url, json=json, headers=headers, cookies=cookies, files=files)
        elif method == "DELETE":
            response = requests.delete(url, json=json, headers=headers, cookies=cookies, files=files)
        else:
            # Raise an exception for an unsupported HTTP method
            raise Exception(f"Bad HTTP method '{method}' was received")

        # Log the response using the Logger class
        Logger.add_response(response)

        # Return the HTTP response object
        return response
