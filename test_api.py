from requests import get, post


def test_api_challenge():
    """
    1.	Do a GET request to the /users endpoint
    2.	Validate the response code to be 200
    3.	Validate the response is an array of json objects
    4.  Write a file named "target_companies.txt" which contains the company names ends with " Group" from the response
    """
    resp = get(url="https://jsonplaceholder.typicode.com/users")
    assert resp.status_code == 200, f"Status Code is {resp.status_code}"
    resp_type = type(resp.json())
    assert resp_type == list, f"response type is {resp_type} "
    match = [d['company']['name'] for d in resp.json() if d['company']['name'].endswith('Group')]
    with open('target_companies.txt', 'w+') as file:
        for line in match:
            file.write("%s\n" % line)


def get_all_available_pets_from_swagger():
    url = "https://petstore3.swagger.io/api/v3/pet/findByStatus"
    payload = {'status': 'available'}
    resp = get(url=url, params=payload)
    return resp.json()


def send_pet_name_in_uppercase(resp):
    for i in resp:
        dog_name = i['name'].upper()
        url = "https://postman-echo.com/post"
        payload = {'name': dog_name}
        resp = post(url=url, params=payload)
        print(resp.json())
        assert resp.status_code == 200, f"postman status code was not 200, is {resp.status_code}"
        assert resp.json()['args']['name'].isupper() == True, "Name is not upper case"
