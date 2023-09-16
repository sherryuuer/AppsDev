def get_the_stock_json(symbol):
    import requests

    STOCK_ENDPOINT = "https://www.alphavantage.co/query"
    STOCK_APIKEY = "6H5CTCZXZPGIH0EA"

    parameters = {
        "function": "TIME_SERIES_DAILY",
        "symbol": symbol,
        "apikey": STOCK_APIKEY,
    }
    url = STOCK_ENDPOINT
    responses = requests.get(url, params=parameters)
    responses.raise_for_status()
    return responses.json()
