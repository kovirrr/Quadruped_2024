from suds.client import Client

user = "novasm3"
passw = "R0botsm3!"
source_DID = "9148280555" #phone number that sends
destination = "9148370362"
msg = "hi this is a robot"

try:
    client = Client('https://backoffice.voipinnovations.com/Services/APIService.asmx?wsdl')
    result = client.service.SendSMS(user, passw, source_DID, destination, msg)
    print("Sent message. Result:", result)
except Exception as e:
    print("An error occurred:", str(e))