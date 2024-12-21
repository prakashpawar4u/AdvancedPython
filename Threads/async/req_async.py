import requests
from concurrent.futures import ThreadPoolExecutor

# The URL of the server
url = "http://localhost:8080"

# Function to send a GET request
def send_request():
    response = requests.get(url)
    print(f"Response Status Code: {response.status_code}")

# Number of requests you want to send concurrently
num_requests = 10

# Use ThreadPoolExecutor to send requests concurrently
with ThreadPoolExecutor(max_workers=num_requests) as executor:
    executor.map(send_request, range(num_requests))
