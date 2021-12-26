# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)

def send_sms(user_code, phone_numer):
	message = client.messages.create(
	                     body=f"Hi! Your user and verification code is {user_code}",
	                     from_='+18124135587',
	                     to=f'+{phone_numer}'
	                 )

	print(message.sid)
