def get_news(company="Tesla"):
    import requests
    from urllib.parse import quote

    endpoint = "https://newsapi.org/v2/everything"
    parameters = {
        "q": quote(company),
        "apiKey": 'd4fcdc1c77f74a8a8074de69a825015f',
    }
    responses = requests.get(url=endpoint, params=parameters)
    responses.raise_for_status()
    articles = responses.json()
    return articles['articles'][0]
