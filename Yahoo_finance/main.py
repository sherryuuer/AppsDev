import pandas as pd
import matplotlib as plt
import yfinance as yf


companies = {
    "apple": "AAPL",
    "facebook": "FB",
    "google": "GOOGL",
    "amazon": "AMZN",
    "microsoft": "MSFT",
}


def get_data(days, tickers):
    df = pd.DataFrame()
    for company in tickers.keys():
        tkr = yf.Ticker(tickers[company])
        hist = tkr.history(period=f'{days}d')
        hist.index = hist.index.strftime('%d %B %Y')
        hist = hist[['Close']]
        hist.columns = [company]
        hist = hist.T
        hist.index.name = 'Name'
        df = pd.concat([df, hist])
    return df


days = 20
data = get_data(days, companies)
data = data.T.reset_index()
data = pd.melt(data, id_vars=["Date"]).rename({"value": "Stock Price(USD)"})
print(data)
