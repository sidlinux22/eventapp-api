from db import db

# Helper class: Internal representation of an entity
class EventModel(db.Model):
    __tablename__ = 'event'
    event_id = db.Column(db.Integer,primary_key=True)
    # ToDO we can declare as datetime object
    eventname = db.Column(db.String(64))  
    # ToDO we can declare as datetime object
    startdate = db.Column(db.String(64))
    enddate = db.Column(db.String(64))
    location = db.Column(db.String(64))
    subscribe_users = db.relationship('UserEventModel', lazy='dynamic')

    def __init__(self, eventname, startdate, enddate, location):
        self.eventname = eventname
        self.startdate = startdate
        self.enddate = enddate
        self.location = location

    def json(self):
        return {'event_id': self.event_id, 'eventname': self.eventname, 'startdate': self.startdate, 'enddate': self.enddate, 'location': self.location, 'subscribe_users': [subscribe_users.json() for subscribe_users in self.subscribe_users.all()]}

# function to find event_id

    @classmethod
    def find_by_event_id(cls, event_id):
        return cls.query.filter_by(event_id=event_id).first()

# function for DB operation 

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
