import requests
from requests.auth import HTTPBasicAuth

YOUR_USERNAME = 'kevchye'
YOUR_PASSWORD = "kevchye"

basic = HTTPBasicAuth('kevchye', 'kevchye')
response = requests.get('https://httpbin.org/basic-auth/kevchye/kevchye', auth=basic)
#requests.get('https://httpbin.org/basic-auth/user/pass', auth=('user', 'pass'))
print(response)

"""# No Authentication
sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)

# Basic Authentication
sheet_response = requests.post(
    sheet_endpoint,
    json=sheet_inputs,
    auth=(
        YOUR_USERNAME,
        YOUR_PASSWORD,
    )
)"""

import os
print(os.environ['HOME'])

