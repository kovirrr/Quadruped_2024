#ALERTS
'''
Location{
Unknown person - RFID + Facial
Motion Detector
}
Maintenance
'''

from suds.client import Client

user = "novasm3"
passw = "R0botsm3!"
source_DID = 19148280555 #phone number that sends
destination = 9148370362
msg = "Hi kovi"

try:
    client = Client('https://backoffice.voipinnovations.com/Services/APIService.asmx?wsdl')
    result = client.service.SendSMS(user, passw, source_DID, destination, msg)
    print("Sent message. Result:", result)
    for item in result:
        print(item)
except Exception as e:
    print("An error occurred:", str(e))