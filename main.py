import requests
from datetime import *

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "icegiant123"
TOKEN = "secretcodeok?"
GRAPH_ID = "graph1"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)


graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Cycling graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

today = datetime(year=2023, month=12, day=18)

post_pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"
pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many kms do you walk today?"),
}

response = requests.post(url=post_pixel_endpoint,json=pixel_data, headers=headers)
print(response.text)

# update_pixel_endpoint = f"{post_pixel_endpoint}/{today.strftime('%Y%m%d')}"
#
# update_data = {
#     "quantity": "9.22"
# }
#
# response = requests.delete(url=update_pixel_endpoint, headers=headers)
# print(response.text)
#

