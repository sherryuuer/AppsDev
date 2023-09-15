# ## Use weather api and twilio to build the project.when your api get the data that forcast rain,a massage will be send to your phone to say take a umbrella.

def get_weather_forcast():
    import requests

    url = "https://api.openweathermap.org/data/2.5/onecall"
    parameters = {
        'lat': 35.652832,
        'lon': 139.839478,
        'exclude': 'hourly,daily',
        'appid': 'xxxxxx',
    }

    responses = requests.get(url, params=parameters)
    responses.raise_for_status()
    data = responses.json()
    return data


def send_message():
    # Use Twilio to send ourself a message. 
    import os
    from twilio.rest import Client

    # use os to get the environment variables to make it safer and not need to change your code when your variables are changed.
    # use same linux command can set your own environment variables.
    # Export xxxx = xxxx
    account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
    auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
    client = Client(account_sid, auth_token)
    client.messages.create(from_=os.environ.get('TWILIO_PHONE_NUMBER'),
                        to=os.environ.get('CELL_PHONE_NUMBER'),
                        body='Get an Umbrella!')


data = get_weather_forcast()
id_list = []
for hour in data["hourly"][:12]:
    for weather in hour["weather"]:
        id_list.append(int(weather["id"]))

# just for test.
# id_list = [900, 400, 800, 701, 390, 670, 690, 900]
will_rain = False
while not will_rain:
    for id in id_list:
        if id < 700:
            send_message()
            # print("get an umbrella")  #Use Twilio to send ourself a message. 
            will_rain = True
            break

# At last automate the code on cloud.like pythonanywhere.
