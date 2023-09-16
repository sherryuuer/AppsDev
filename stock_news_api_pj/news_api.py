def get_news(company="Tesla"):
    import requests
    from urllib.parse import quote

    endpoint = "https://newsapi.org/v2/everything"
    parameters = {
        "q": quote(company),
        "apiKey": 'my_key',
    }
    responses = requests.get(url=endpoint, params=parameters)
    responses.raise_for_status()
    articles = responses.json()
    return articles['articles'][0]
