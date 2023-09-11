# pip install requests
import requests


url = "http://api.open-notify.org/iss-now.json"
responses = requests.get(url=url)
# print(responses.status_code)  # 200 means success
# from doc
# https://requests.readthedocs.io/en/latest/
responses.raise_for_status()
data = responses.json()
longitude = data["longitude"]
latitude = data["latitude"]
iss_position = (longitude, latitude)
# longitude and latitude can address a position on the earth.
# use this: https://www.latlong.net/Show-Latitude-Longitude.html


