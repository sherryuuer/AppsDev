def send_message_to_slack(message):
    from slack_sdk.webhook import WebhookClient

    url = "https://hooks.slack.com/services/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"
    webhook = WebhookClient(url)

    response = webhook.send(text=message)
    assert response.status_code == 200
    assert response.body == "ok"
