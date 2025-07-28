from flask import Flask, request, render_template, redirect, url_for
from twilio.rest import Client
import os

app = Flask(__name__)

# Load phone numbers in memory
phone_numbers = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        number = request.form.get('number')
        message = request.form.get('message')
        selected = request.form.getlist('selected')

        if number:
            phone_numbers.append(number)

        if message and selected:
            # Twilio credentials from environment
            account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
            auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
            from_number = os.environ.get('TWILIO_PHONE_NUMBER')

            client = Client(account_sid, auth_token)

            for num in selected:
                client.messages.create(
                    to=num,
                    from_=from_number,
                    body=message
                )
        return redirect(url_for('index'))

    return render_template('index.html', phone_numbers=phone_numbers)

if __name__ == '__main__':
    app.run(debug=True)
