import datetime
import os
from requests import Response


class Logger:
    # Define the log file name based on the current date and time
    file_name = f"logs/log_" + str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")) + ".log"

    @classmethod
    def _write_log_to_file(cls, data):
        try:
            # Open the log file and append data to it
            with open(cls.file_name,  'a', encoding='utf-8') as logger_file:
                logger_file.write(data)
        except FileNotFoundError:
            # Handle the case where the log file is not found
            print("File log not found")

    @classmethod
    def add_request(cls, url, data, headers, cookies, method, files):
        # Get the current test name from the environment
        testname = os.environ.get('PYTEST_CURRENT_TEST')

        # Create data to log for the request
        data_to_add = f"\n-----\n"
        data_to_add += f"Test: {testname}\n"
        data_to_add += f"Time: {str(datetime.datetime.now())}\n"
        data_to_add += f"Request method: {method}\n"
        data_to_add += f"Request URL: {url}\n"
        data_to_add += f"Request data: {data}\n"
        data_to_add += f"Request headers: {headers}\n"
        data_to_add += f"Request cookies: {cookies}\n"
        data_to_add += f"Request files: {files}\n"
        data_to_add += "\n"

        # Write the request data to the log file
        cls._write_log_to_file(data_to_add)

    @classmethod
    def add_response(cls, response: Response):
        # Convert cookies and headers to dictionaries for logging
        cookies_as_dict = dict(response.cookies)
        headers_as_dict = dict(response.headers)

        # Create data to log for the response
        data_to_add = f"Response code: {response.status_code}\n"
        data_to_add += f"Response text: {response.text}\n"
        data_to_add += f"Response headers: {headers_as_dict}\n"
        data_to_add += f"Response cookies: {cookies_as_dict}\n"
        data_to_add += "\n-----\n"

        # Write the response data to the log file
        cls._write_log_to_file(data_to_add)