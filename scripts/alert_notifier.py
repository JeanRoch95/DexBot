from twilio.rest import Client

def send_sms_alert(token_name, token_price):
    account_sid = 'your_account_sid'
    auth_token = 'your_auth_token'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=f"Token {token_name} a atteint {token_price} USD.",
        from_='+1234567890',  # Votre numéro Twilio
        to='+0987654321'  # Numéro de destination
    )

    print(f"SMS envoyé : {message.sid}")

if __name__ == "__main__":
    token_name = "SOL"
    token_price = 150
    send_sms_alert(token_name, token_price)
