import os
import json
from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)

# Configure mail settings
app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # Change this to your email provider's SMTP server
app.config['MAIL_PORT'] = 587  # Change the port if needed
app.config['MAIL_USE_TLS'] = True  # Enable Transport Layer Security (TLS)
app.config['MAIL_USERNAME'] = 'scsavailable@gmail.com'  # Your email address
app.config['MAIL_PASSWORD'] ='hjas zyfg ggxu vaax' #ieqq hrdz ioss nklh''  # Your email password or app-specific password
app.config['MAIL_DEFAULT_SENDER'] = 'Client@gmail.com'  # Your default sender email address


mail = Mail(app)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/client')
def client():
    return render_template('client.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

#read more

@app.route('/readabout')
def readabout():
    return render_template('readabout.html')

@app.route('/quote')
def quote():
    return render_template('quote.html')

@app.route('/readmore')
def readmore():
    return render_template('readmore1.html')


@app.route('/thanks', methods=['POST'])
def thanks():
    if request.method == 'POST':
        name = request.form['Name']
        if request.method == 'POST':

            phone = request.form['Phone Number']
            if request.method == 'POST':
                email = request.form['Email Address']
                if request.method == 'POST':
                    message = request.form['Massage']
                    msg = Message('New message from your website', recipients=['viveksinghpihuli0a@gmail.com'])  # Your email address to receive messages
                    msg.body = f"Name: {name}\nPhone: {phone}\nEmail: {email}\nMessage: {message}"

                    # Send the email
                    mail.send(msg)

                    return render_template('thankyou.html')
                else:
                    return "Error sending email!  Please Try Again"

                    # Compose email
            else:
                return 'Please Enter Your Valid Email!'
        else:
            return 'Please Enter Your Phone Number!'

    return 'Please Enter Your Name'

if __name__ == "__main__":
    app.run(debug=True)

