from twilio.rest import Client

account_sid = ''
auth_token = '[]'
client = Client(account_sid, auth_token)

message = client.messages.create(from_ = '1111111111', #Twilio-enabled phone #
                                 body = 'Hi',
                                 to= '0000000000')

print(message.sid)