from suds.client import Client
import geocoder
import time
import random

user = "novasm3"
passw = "R0botsm3!"
source_DID = 19148280555 #phone number that sends
destination = 19148370362 #phone number that gets texted (security)
msg = "testing"

detections = [] #list of every detection. go to detect_person function
threat_level = 0 #current threat level. (0-3, 0 being least and 3 most)
last_update = 0 #arbitrary number
delay_time = 10 #how often the status of the robot is updated to security (in seconds)

def detect_person(threat_level=threat_level):
     #uses the facial recognition and RFID detection
     #threat level can only go back down when overridden


    if 1==2 and threat_level < 1: #if someone is detected but RFID and facial recognition work
        threat_level = 1 #do nothing. just ignore
    elif 1==3 and threat_level < 2: #if someone is detected and RFID works but not facial recognition
        threat_level = 2 #worth looking at
    elif 1==4 and threat_level < 3: #if someone is detected but RFID and facial recognition don't work
        threat_level = 3 #sound alarm

    info = "" #infortmation about the detection
    if threat_level != 0:
        detections.append((time.time(), threat_level, info)) #tuple of 3 things: when detected, threat level, info about it
        return f"Threat Detected: Level {threat_level}"
    return "No threat detected"

def cur_location():
    g = geocoder.ip('me')
    location = g.latlng
    rString = "Current Location: "
    for i in range(2):
        rString += str(location[i])
        rString += " "
    
    #print(rString)
    return rString

def status():
    rStr = "Status: "
    detect_person()
    if threat_level == 0:
        rStr += "Neutral"
    else:
        rStr += f"Threat Detected! (Level {threat_level})"
    return rStr

def update():
    return f"{cur_location()}\n{status()}\n{get_time()}"

def send_message(message):
    try:
        client = Client('https://backoffice.voipinnovations.com/Services/APIService.asmx?wsdl')
        result = client.service.SendSMS(user, passw, source_DID, destination, message)
        return result
    except Exception as e:
        print("error:", str(e))
        return None
    
def check_response():
    #find a way to get the security guard to text the number and for it to get picked up
    return None

def get_time():
    current = time.localtime()
    return f"Time: {current.tm_year}-{current.tm_mon:02d}-{current.tm_mday:02d} {current.tm_hour:02d}:{current.tm_min:02d}:{current.tm_sec:02d}"

last_update = time.time()
while 1:
    if time.time() - last_update >= delay_time:
        print("updating...")
        send_message(update()) #update every delay_time (in seconds)
        last_update = time.time()

    #constantly check for the security guard texting
    response = check_response()
    if response: #if it senses anything
        if response == "update" or response == "u":
           send_message(update())
        elif response == "reset" or response =="r": #the securty guard sees what the robot senses and is confirming that everything is ok
              threat_level = 0
              send_message("Successfuly reset threat level")