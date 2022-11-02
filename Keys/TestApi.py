import json

from robot.libraries.BuiltIn import BuiltIn
from requests import get, post
from Vars.Urls import challenge2_url


class TestApi:
    def __init__(self):
        """
        1.	Do a GET request to the /users endpoint
        2.	Validate the response code to be 200
        3.	Validate the response is an array of json objects
        4.  Write a file named "target_companies.txt" which contains the company names ends with " Group" from the response
        """
        self.bi = BuiltIn()

    def base_request_api(self, url, method=get, param=None):
        resp = method(url=url, params=param)
        # self.bi.log_to_console(resp)
        return resp

    def get_response_url_api(self, url):
        resp = self.base_request_api(url, method=get)
        return resp

    def validate_json_data_is_an_array(self, json_data):
        data_type = type(json_data.json())
        assert data_type == list, f"response type is {data_type} "

    def find_and_write_company_name_from_response(self, response):
        match = [d['company']['name'] for d in response.json() if d['company']['name'].endswith('Group')]
        with open('target_companies.txt', 'w+') as file:
            for line in match:
                self.bi.log_to_console(line)
                file.write("%s\n" % line)

    def get_all_available_pets(self):
        url = challenge2_url + "/api/v3/pet/findByStatus"
        payload = {'status': 'available'}
        resp = self.base_request_api(url=url, param=payload)
        return resp.json()

    def send_pet_name_in_uppercase_and_assert(self, resp):
        for i in resp:
            dog_name = i['name'].upper()
            url = "https://postman-echo.com/post"
            payload = {'name': dog_name}
            response = self.base_request_api(url=url, method=post, param=payload)
            # self.bi.log_to_console(response.json())
            assert response.status_code == 200, f"postman status code was not 200, is {resp.status_code}"
            assert response.json()['args']['name'].isupper() == True, f"{response.json()['args']['name']} " \
                                                                      f"Name is not upper case"
