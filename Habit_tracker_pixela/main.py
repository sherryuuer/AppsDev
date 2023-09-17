import requests
import datetime


TOKEN = "uniznr&jinju4haku"
USER_NAME = "sallyw"
GRAPH_ID = "graph1"
date_today = datetime.datetime.now().strftime("%Y%m%d")
pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"
pixe_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}"
update_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{date_today}"
delete_endpoint = update_endpoint

# create a user.
# user_params = {
#     "token": TOKEN,
#     "username": USER_NAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes",
#     }
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)
# {"message":"Success. Let's visit https://pixe.la/@sallyw , it is your profile page!","isSuccess":true}

# create a graph.
headers = {
    'X-USER-TOKEN': TOKEN,
}
# graph_params = {
#     "id": GRAPH_ID,
#     "name": "Coding Graph",
#     "unit": "hour",
#     "type": "float",
#     "color": "ajisai",
#     "timezone": "Asia/Tokyo",
#     }
# response = requests.post(url=graph_endpoint, headers=headers, json=graph_params)
# print(response.text)
# {"message":"Success.","isSuccess":true}

# post a pixela of today.
pixe_params = {
    "date": date_today,
    "quantity": input("How many hours did you code today? "),
    "optionalData": "{\"contents\":\"100daycode and leetcode\"}",
    }
response = requests.post(url=pixe_endpoint, headers=headers, json=pixe_params)
print(response.text)
# {"message":"Success.","isSuccess":true}

# use put to update a pixela.
# update_params = {
#     "quantity": "3",
#     "optionalData": "{\"contents\":\"100daycode and leetcode\"}",
#     }
# print(update_endpoint)
# response = requests.put(url=update_endpoint, headers=headers, json=update_params)
# print(response.text)
# https://pixe.la/v1/users/sallyw/graphs/graph1/20230917
# {"message":"Success.","isSuccess":true}

# use delete to delete a pixela.
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)
# {"message":"Success.","isSuccess":true}
