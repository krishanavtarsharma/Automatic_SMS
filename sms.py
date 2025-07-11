from twilio.rest import Client

# ---------------------------------
# ✅ Twilio Credentials (replace with yours)
account_sid = 'YOUR_ACCOUNT_SID'        # Example: 'ACxxxxxxxxxxxxxxxxxxxxxxx'
auth_token = 'YOUR_AUTH_TOKEN'          # Example: 'a1b2c3d4e5f6gj0'
twilio_number = '+123456....'           # Your Twilio phone number (with + and country code)
receiver_number = '+91XXXXXXXX'       # Recipient's number (with country code)

# ---------------------------------
# ✉️ Message Content
message_body = 'Hello! This is a test message from my Python SMS automation app.'

# ---------------------------------
# ✅ Send SMS
try:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=message_body,
        from_=twilio_number,
        to=receiver_number
    )

    print(f"✅ SMS sent successfully! Message SID: {message.sid}")

except Exception as e:
    print(f"❌ Error sending SMS: {e}")
