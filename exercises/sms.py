# Account SID: AC3f362fda5d022ef9fac202276fc28607
# Auth Token: 4dd8cd4be8aa1f5dd0a2733ca9d67690
# Twilio Phone Number: +13853964799

# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'AC3f362fda5d022ef9fac202276fc28607'
auth_token = '4dd8cd4be8aa1f5dd0a2733ca9d67690'
client = Client(account_sid, auth_token)

message = client.messages.create(
  body="Join Earth's mightiest heroes. Like Kevin Bacon.",
  from_='+13853964799',
  to='+5218180545002'
)

print(message.sid)