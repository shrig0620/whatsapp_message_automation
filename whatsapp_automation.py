import pywhatkit
import time
from datetime import datetime

# List of phone numbers (including country code)
contacts = [
    "+919080109689", #Enter numbers with country code
    "+910123456789",
    "+911234567890"
    ]

# Message to send
message = "Hello! This is an automated message from SHRI.G"

# Get current time
now = datetime.now()

# Loop through each contact and send the message immediately
for index, contact in enumerate(contacts):
    # Calculate the time for sending (next available minute)
    minute_to_send = now.minute + 1 + index  # Increment minutes for each contact

    # If minutes exceed 59, adjust the hour and wrap around minutes
    hour_to_send = now.hour
    if minute_to_send >= 60:
        hour_to_send += minute_to_send // 60
        minute_to_send = minute_to_send % 60

        if hour_to_send >= 24:
            hour_to_send = 0  # Wrap around for hours

    # Send message
    pywhatkit.sendwhatmsg(contact, message, hour_to_send, minute_to_send)

    # Wait for a longer period to ensure the message is sent before sending the next one
    time.sleep(15)  # Wait for 15 seconds or more to allow WhatsApp to process the message
