import os
from twilio.rest import Client

# Load credentials from Render environment variables
TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH = os.getenv("TWILIO_AUTH")
TWILIO_PHONE = os.getenv("TWILIO_PHONE")

client = Client(TWILIO_SID, TWILIO_AUTH)

# List of recipient phone numbers
recipients = [
    "+17867848466",
    "+13526829932",
    "+19107286226"
]

# Message to send
message_body = "Hello! This is a test message from your Render-deployed Python app 🎉"

# Send the SMS
for recipient in recipients:
    message = client.messages.create(
        to=recipient,
        from_=TWILIO_PHONE,
        body=message_body
    )
    print(f"Sent to {recipient}: {message.sid}")
