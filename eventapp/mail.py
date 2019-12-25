# Using Flask-RESTful so no need to use jsonify!
from flask import Flask
from flask_jwt import JWT
from flask_restful import Api
import json
from flask_mail import Mail, Message

# Send mail for new subscription

class MailNotify():
    @classmethod
    def send_mail(cls,email):
        app = Flask(__name__)
        with open('config.json') as config_file:
            config_data = json.load(config_file)
        mail_settings = config_data['mail_settings']
        app.config.update(mail_settings)
        mail = Mail(app)
        msg = Message("Welcome to Eventapp!",
                      sender=app.config['MAIL_USERNAME'],
                        recipients=[email])
        msg.body = "Thanks for subscribing this event!:)"
        if app.config['ENABLE_NOTIFICATION']:
           mail.send(msg)
