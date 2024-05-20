import requests

# Define the data to be sent in the request
data = {'clickid': '1000'}

# Send the POST request with form data
response = requests.post('http://0.0.0.0:8000/click/', data=data, timeout=600)

# Print the response from the server
print(response.status_code)
print(response.json())