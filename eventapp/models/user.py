import sqlite3
from db import db
import re
from flask_mail import Mail, Message

# regex pattern for input email validation
email_regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

# Helper class: Internal representation of an entity
class UserModel(db.Model):
    __tablename__ = 'users'
    email = db.Column(db.String(80), primary_key=True)
    username = db.Column(db.String(80))

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def json(self):
        return {'username': self.username, 'email': self.email}
        
# function to find input username 
    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

# function to find input email 
    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

# function to valid email 
    @classmethod
    def valid_user_email(cls, email):
        return re.search(email_regex, email)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
