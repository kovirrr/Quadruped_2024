from suds.client import Client
import geocoder
import time

user = "novasm3"
passw = "R0botsm3!"
source_DID = 19148280555 #phone number that sends
destination = 19087208484
msg = "testing"

def cur_location():
    g = geocoder.ip('me')
    return g.latlng

def send_message(message):
    try:
        client = Client('https://backoffice.voipinnovations.com/Services/APIService.asmx?wsdl')
        result = client.service.SendSMS(user, passw, source_DID, destination, message)
        return result
    except Exception as e:
        print("error:", str(e))
        return None
    
while 1:
    print(cur_location())
    time.sleep(1)