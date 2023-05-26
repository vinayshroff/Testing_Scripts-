import requests
import json

def test_api(api_url, test_cases_file):
    # Load test cases from JSON file
    with open(test_cases_file, 'r') as f:
        test_cases = json.load(f)

    # Iterate over test cases
    for test_case in test_cases:
        # Extract test case data
        name = test_case['name']
        method = test_case['method']
        endpoint = test_case['endpoint']
        headers = test_case.get('headers', {})
        params = test_case.get('params', {})
        expected_status = test_case.get('expected_status')
        expected_response = test_case.get('expected_response')

        # Prepare request URL
        url = api_url + endpoint

        # Send the API request
        response = requests.request(method, url, headers=headers, params=params)

        # Check the response status code
        if expected_status is not None:
            assert response.status_code == expected_status, f"{name}: Expected status {expected_status}, but got {response.status_code}"

        # Check the response data
        if expected_response is not None:
            response_data = response.json()
            assert response_data == expected_response, f"{name}: Expected response {expected_response}, but got {response_data}"

        # Test case passed
        print(f"{name}: PASSED")

# Example usage
api_url = 'https://api.example.com'
test_cases_file = 'test_cases.json'
test_api(api_url, test_cases_file)
