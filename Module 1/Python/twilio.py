from twilio.rest import TwilioRestClient

account_sid = "AC35db667c505091a095030979d636b16d"
auth_token = "790500f2fea9093c1b385a795ed51e88"

# creating a client
client = TwilioRestClient(account_sid, auth_token)

# creating message.
message = client.sms.message.create(
	body = "Testing Twilio, Bitch",
	to = "+919962130574",
	from_ = "+919962130574",
);
print (message.sid)