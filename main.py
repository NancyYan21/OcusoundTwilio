import os
from datetime import datetime, timedelta
from twilio.rest import Client
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
messaging_service_sid = os.getenv('TWILIO_MSG_SRVC_SID')

client = Client(account_sid, auth_token)

def schedule_message(to, body, minutes_from_now):
    send_at = (datetime.utcnow() + 
timedelta(minutes=minutes_from_now)).isoformat() + 'Z'
    message = client.messages.create(
        messaging_service_sid=messaging_service_sid,
        to=to,
        body=body,
        schedule_type='fixed',
        send_at=send_at
    )
    print(f"Scheduled message SID: {message.sid}")

# Schedule a message
schedule_message('+14692376410', 'Hello, this is a scheduled message!', 6)

