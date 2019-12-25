from sqlalchemy import and_, or_, not_
from db import db

# Helper class: Internal representation of an entity

class UserEventModel(db.Model):
     __tablename__ = 'userevent'
     id = db.Column(db.Integer, primary_key=True)
     event_id = db.Column(db.Integer, db.ForeignKey('event.event_id'))
     event = db.relationship('EventModel')
     email = db.Column(db.String(80))

     def __init__(self, event_id, email):
        self.event_id = event_id
        self.email = email

     def json(self):
        return {'id': self.id, 'event_id': self.event_id, 'email': self.email}

# function to find input email
     @classmethod
     def find_by_event_id(cls, event_id):
        return cls.query.filter_by(event_id=event_id).first()

# function to validate Duplicate subscriptions)
     @classmethod
     def check_by_event_id_email(cls, event_id, email):
        result = cls.query.filter_by(event_id=event_id).filter_by(email=email).first()
        return result
 
# function for DB operation 

     def save_to_db(self):
        db.session.add(self)
        db.session.commit()

     def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
