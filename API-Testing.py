import requests

# API base URL
base_url = "https://api.example.com"

# Function to send API requests and validate the responses
def test_api(endpoint, method, payload=None):
    url = base_url + endpoint

    # Send the API request
    if method == "GET":
        response = requests.get(url)
    elif method == "POST":
        response = requests.post(url, json=payload)
    elif method == "PUT":
        response = requests.put(url, json=payload)
    elif method == "DELETE":
        response = requests.delete(url)
    else:
        print("Invalid HTTP method:", method)
        return

    # Validate the response
    if response.status_code == 200:
        print(f"Test case passed! [{method} {endpoint}]")
        # Additional validation logic can be added here
    else:
        print(f"Test case failed! [{method} {endpoint}]")
        print("Response:", response.text)


# Test Cases
test_api("/users", "GET")  # Test GET request to /users endpoint
test_api("/users", "POST", {"name": "John", "email": "john@example.com"})  # Test POST request to /users endpoint with payload
test_api("/users/123", "PUT", {"name": "John Doe"})  # Test PUT request to /users/123 endpoint with payload
test_api("/users/123", "DELETE")  # Test DELETE request to /users/123 endpoint
