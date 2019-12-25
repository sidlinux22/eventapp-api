from flask_jwt import jwt_required
from flask_restful import Resource, reqparse
from models.event import EventModel
import datetime

# Resource class: External representation of an entity
class Event(Resource):
    # Using reqparse
    parser = reqparse.RequestParser()
    parser.add_argument('eventname', type=str, required=True, help="This field cannot be blank")
    parser.add_argument('startdate', type=str, required=True,help="This field cannot be blank")
    parser.add_argument('enddate', type=str, required=True,help="This field cannot be blank")
    parser.add_argument('location', type=str, required=True,help="This field cannot be blank")

#  create a new event
    def post(self):
        data = Event.parser.parse_args()
        event_data = EventModel(data['eventname'],data['startdate'], data['enddate'], data['location'])
        try:
            event_data.save_to_db()
        except:
            return {'message': 'An error occurred while creating the new event'}, 500
            
        return event_data.json(), 201

class EventSearch(Resource):

# Find and response requested event
    def get(self, event_id):
        event_data = EventModel.find_by_event_id(event_id)
        if event_data:
            return event_data.json()
        return {'message': "event_id not found"}, 404

# Delete requested event
    def delete(self, event_id):
        event_data = EventModel.find_by_event_id(event_id)
        if not event_data:
            return {'message': "event_id not found"}, 404
        try:
            event_data.delete_from_db()
        except:
            return {'message': 'Internal error occurred while deleting event'}, 500
        return {'message': "Event deleted"}, 200

# list of all events
class EventList(Resource):
    def get(self):
        return {'events': [store.json() for store in EventModel.query.all()]}
