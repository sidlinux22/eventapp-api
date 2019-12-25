from flask_jwt import jwt_required
from flask_restful import Resource, reqparse
from models.userevent import UserEventModel
from models.user import UserModel
from models.event import EventModel


# Resource class: External representation of an entity

class UserEvent(Resource):
    # Using reqparse
    parser = reqparse.RequestParser()
    parser.add_argument('event_id', type=int, required=True, help="This field cannot be blank")
    parser.add_argument('email', type=str, required=True,
                        help="Every item needs a email")

    def parseData(self):
        userevent_data = UserEvent.parser.parse_args()
        userevent_model = UserEventModel(
            userevent_data['event_id'], userevent_data['email'])
        return userevent_data

# Subscribe Event

    def post(self):
#### userevent data
        userevent_data = UserEvent.parser.parse_args()
        userevent_model = UserEventModel(
            userevent_data['event_id'], userevent_data['email'])

        try:

            # validate if email if is valid 
            if not UserModel.find_by_email(userevent_data['email']):
                return {'message': "Invalid email '{}'".format(userevent_data['email'])}, 409

            # Validate if event Id is valid                 
            if not EventModel.find_by_event_id(userevent_data['event_id']):
               return {'message': "Invalid event_id '{}'".format(userevent_data['event_id'])}, 409

            # Validate if event Id and email with userevent
            if UserEventModel.check_by_event_id_email(userevent_data['event_id'], userevent_data['email']):
               return {'message': "user email '{}' has already subscribe this event_id '{}'".format(userevent_data['email'], userevent_data['event_id'])}, 409

            userevent_model.save_to_db()
        except:
            return {'message': "An error occurred subscribing event_id '{}'".format(userevent_data['event_id'])}, 500

        return userevent_model.json(), 201

# Unsubscribe event

    def delete(self):
        userevent_data=self.parseData()
        try:
            if not UserEventModel.check_by_event_id_email(userevent_data['event_id'], userevent_data['email']):
                return {'message': "Invalid event_id '{}' or email '{}' ".format(userevent_data['event_id'], userevent_data['email'])}, 403
            user_event = UserEventModel.find_by_event_id(
            userevent_data['event_id'])
            user_event.delete_from_db()
        except:
            return {'message': "An error occurred unsubscribing event_id '{}'".format(userevent_data['event_id'])}, 500
        return {'message': "User email '{}' unsubscribe event_id '{}'".format(userevent_data['email'], userevent_data['event_id'])}, 200


# List all events with user subscription 
class UserEventList(Resource):
    def get(self):
        return {'user_events': [event.json() for event in UserEventModel.query.all()]}
