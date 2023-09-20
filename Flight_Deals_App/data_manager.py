import requests
import flight_search_key


SHEETY_ENDPOINT = "https://api.sheety.co/f12e654105095c2388e43575f5eb5977/swFlightDeals/prices"
BEARER_TOKEN = flight_search_key.sheety_bearer


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}

    def get_destination(self):
        response = requests.get(url=SHEETY_ENDPOINT)
        data = response.json()
        return data

    def put_destination(self):
        for data in self.destination_data:
            city = data["city"]
            iataCode = data["iataCode"]
            lowestPrice = data["lowestPrice"]
            id = data["id"]
            headers = {
                'Authorization': f'Basic {BEARER_TOKEN}'
            }
            sheety_params = {
                "price": {
                    "city": city,
                    "iataCode": iataCode,
                    "lowestPrice": lowestPrice,
                }
            }
            sheet_response = requests.put(url=f"{SHEETY_ENDPOINT}/{id}", headers=headers, json=sheety_params)
            print(sheet_response.text)
