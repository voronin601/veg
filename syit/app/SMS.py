import os
from twilio.rest import Client
import random

char = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']
krypt = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']

def enter_SMS(Num, sms):
    account_SID = os.environ["TWILIO_ACCOUNT_SID"]
    auth_token = os.environ["TWILIO_AUTH_TOKEN"]
    
    client = Client(account_SID, auth_token)

    client.messages.create(
        to = form_num(Num),
        from_ = "+12014925702",
        body = sms
    )

def form_num(num):
    if num[:1]!="+": return "+7" + num[1:]
    return num

def kript():
    return (''.join([krypt[random.randint(0, len(char)-1)] for i in range(0,6)]))

def KOD():
    #return (char[random.randint(0, len(char)-1)] + char[random.randint(0, len(char)-1)] + char[random.randint(0, len(char)-1)] + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)))
    return char[random.randint(0, len(char)-1)]