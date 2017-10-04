from twilio.rest import TwilioRestClient

account_sid = "AC35db667c5XXXXXXXXXXXXXXXXXX"
auth_token = "790500XXXXXXXXXXXXXXXXXXXXXXXX"

# creating a client
client = TwilioRestClient(account_sid, auth_token)

# creating message.
message = client.sms.message.create(
	body = "Testing Twilio, Bitch",
	to = "+919XXXXXXXXX",
	from_ = "+9199XXXXXXXXXXXX",
);
print (message.sid)
