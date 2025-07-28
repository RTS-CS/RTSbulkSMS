import os
from flask import Flask, request, render_template
from twilio.rest import Client

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/send_sms', methods=['POST'])
def send_sms():
    numbers = request.form.get('numbers', '').split(',')
    message = request.form.get('message', '').strip()

    account_sid = os.getenv("TWILIO_ACCOUNT_SID")
    auth_token = os.getenv("TWILIO_AUTH_TOKEN")
    from_number = os.getenv("TWILIO_PHONE_NUMBER")

    if not (account_sid and auth_token and from_number):
        return "⚠️ Missing Twilio credentials"

    client = Client(account_sid, auth_token)

    for num in numbers:
        num = num.strip()
        if num:
            client.messages.create(
                to=num,
                from_=from_number,
                body=message
            )

    return f"✅ Message sent to: {', '.join(numbers)}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
