import requests
from datetime import datetime

"""for reference and guidance https://pixe.la/
https://docs.pixe.la/entry/post-user
https://pixe.la/v1/users/kevchye/graphs/graph1.html"""

pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = "hsdfe3334nsd" # random string with length from 8-128 see the requirement in api document
USER_NAME = "kevchye" # random username that's not being used
GRAPH_ID = "graph1" # a random name for your graph

user_params ={
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

"""
# step 1: 
delete after creating your own account 
response = requests.post(url=pixela_endpoint, json=user_params)
print(response.json())
print(response.text)
"""

graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"

graph_config = {
    "id" : GRAPH_ID,
    "name": "Coding Graph",
    "unit" : "uploads",
    "type" : "int",
    "color" : "ajisai"
}

headers = {
    "X-USER-TOKEN" :TOKEN
}
"""
# step 2:
delete after creating your own empty graph
response = requests.post(url=graph_endpoint, json=graph_config, headers= headers)
print(response.text)
"""

pixel_creation_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}"

today = datetime.now()
print(today)

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many kilometers did you cycle today? "),

}

"""response = requests.post(url=pixel_creation_endpoint,json=pixel_data, headers=headers)
print(response.text)"""

update_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "40"
}

response = requests.put(url=update_endpoint, json=new_pixel_data,headers=headers)
print(response.text)

"""
## PUT
# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)

delete_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

## DELETE
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)
"""
