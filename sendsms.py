from twilio.rest import Client
import os

def sendSMS(name):
    account_sid = "AC0d211a1b3bbfa83889c8fdb96c6f626c"
    auth_token = "3445eda1548535823c18f40b6853a1fa"
    client = Client(account_sid, auth_token)
    message = client.messages.create(
                              body = name+' Spotted out side the class',
                              from_ = '+12706123142',
                              to = '+918056498279'
                          )

sendSMS("Jeff")