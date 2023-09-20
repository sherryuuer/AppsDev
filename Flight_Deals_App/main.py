# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
# from notification_manager import NotificationManager

data_manager = DataManager()
destination_data = data_manager.get_destination()["prices"]
flight_search = FlightSearch()
print(destination_data)

ORIGIN_CITY_IATA = "TYO"
tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in destination_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    if flight.price < destination["lowestPrice"]:
        # notification_manager.send_sms(
        message = f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
        # )
        print(message)

# if destination_data[0]["iataCode"] == "":
#     from flight_search import FlightSearch
#     flight_search = FlightSearch()
#     for row in destination_data:
#         row["iataCode"] = flight_search.get_destination_code(row["city"])
#     print(destination_data)

#     data_manager.destination_data = destination_data
#     data_manager.put_destination()
