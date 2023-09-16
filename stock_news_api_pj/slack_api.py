def send_message_to_slack(message):
    from slack_sdk.webhook import WebhookClient

    url = "https://hooks.slack.com/services/xxxxxxxxxx/xxxxxxxxx/xxxxxxxxxxxxxxx"
    webhook = WebhookClient(url)

    response = webhook.send(text=message)
    assert response.status_code == 200
    assert response.body == "ok"
