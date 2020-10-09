"""
from twilio.rest import Client 
 
account_sid = 'ACa2a718b3d38cf8c4837fda60399c1d5c' 
auth_token = '632517137d23001cc56a87f1c7de5c16' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='+19094747423',  
                              body='Ahoj ty idiote ',      
                              to='+420735280000' 
                          ) 
 
print(message.sid)


"""

# Download the helper library from https://www.twilio.com/docs/python/install

textFile = open("textMessageLog", "w")

from twilio.rest import Client

account_sid = 'ACa2a718b3d38cf8c4837fda60399c1d5c'
auth_token = '632517137d23001cc56a87f1c7de5c16'
client = Client(account_sid, auth_token)

messages = client.messages.list(limit=20)

for record in messages:
    print(record.sid)
    textFile.write(f"Message: {record.sid}\n")
textFile.close()