from flask import Flask
from flask_jwt import JWT
from flask_restful import Api
from resources.user import UserRegister, UserList
from resources.userevent import UserEvent, UserEventList
from resources.event import Event, EventList, EventSearch
from flask_mail import Mail, Message


app = Flask(__name__)
api = Api(app)

# DB config settings
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'fomenky'

mail = Mail(app)

@app.before_first_request
def create_tables():
    db.create_all()

# API endpoints 
api.add_resource(UserRegister, '/v1/register')    # POST
api.add_resource(UserList, '/v1/users')     # GET
api.add_resource(Event, '/v1/event')        # POST
api.add_resource(EventSearch, '/v1/event/<int:event_id>')   # GET DELETE
api.add_resource(EventList, '/v1/events')      # GET
api.add_resource(UserEvent, '/v1/subscribe')   # POSTs # DELETE
api.add_resource(UserEventList, '/v1/subscribe/users')   #GET

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)




