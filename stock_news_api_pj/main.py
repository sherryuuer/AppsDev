from datetime import datetime, timedelta
from stock_api import get_the_stock_json
from news_api import get_news
from slack_api import send_message_to_slack


STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla"
STOCK_SYMBOL = "TSLA"

# get yesterday datetime
current_date = datetime.now()
yesterday = current_date - timedelta(days=1)
yesterday = yesterday.strftime("%Y-%m-%d")
before_yesterday = current_date - timedelta(days=2)
before_yesterday = before_yesterday.strftime("%Y-%m-%d")

# calculate the stock diff
data = get_the_stock_json(STOCK_SYMBOL)
yesterday_close = data["Time Series (Daily)"][yesterday]["4. close"]
before_yesterday_close = data["Time Series (Daily)"][before_yesterday]["4. close"]
percent_diff = abs(float(yesterday_close) - float(before_yesterday_close)) / float(before_yesterday_close) * 100

if float(yesterday_close) - float(before_yesterday_close) > 0:
    mark = "▲"
else:
    mark = "▼"

# get news
if percent_diff > 0:  # for test # 5
    recent_news = get_news(COMPANY_NAME)
    headline = recent_news["title"]
    brief = recent_news["description"]
    url = recent_news["url"]

    message_formatted = f"{STOCK_NAME}: {mark}{percent_diff}\nHeadline: {headline}\nBrief:{brief}"
    # print(message_formatted)
    send_message_to_slack(message_formatted)





# the instruction from Angela for a backup.
# Instead of using twilio, I am going to use slack to test the error I met last week.
    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
#TODO 2. - Get the day before yesterday's closing stock price
#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 
#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
#TODO 9. - Send each article as a separate message via Twilio. 
#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

