import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import time

# Initialize the RFID reader
reader = SimpleMFRC522()

print("RFID Reader initialized. Waiting for tags...")

try:
    while True:
        # Wait for a tag to be detected
        id, text = reader.read()
        
        print("Tag detected!")
        print(f"ID: {id}")
        print(f"Text: {text}")
        
        # Wait a bit before reading again
        time.sleep(2)

except KeyboardInterrupt:
    print("Program stopped by user")

finally:
    # Clean up GPIO
    GPIO.cleanup()