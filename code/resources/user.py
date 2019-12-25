import sqlite3
from flask_restful import Resource, reqparse
from mail import MailNotify
from models.user import UserModel


# Resource class: External representation of an entity
class UserRegister(Resource):
# Using reqparse
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True, help="This field cannot be blank")
    parser.add_argument('email', type=str, required=True, help="This field cannot be blank")

 # register new user
    def post(self):
        user_data = UserRegister.parser.parse_args()

        if UserModel.find_by_email(user_data['email']):
            return {'message': "User with email '{}' already  exists  ".format(user_data['email'])}, 409

        if not UserModel.valid_user_email(user_data['email']):
            return {'message': "Invalid email '{}'".format(user_data['email'])}, 422  
        user = UserModel(**user_data)
        try:
            user.save_to_db()
        except:
            return {'message': "An error occurred registering user"}, 500
        mailnotify = MailNotify()
        mailnotify.send_mail(user_data['email'])
        return {'message': 'User created successfully'}, 201

# Delete registered user
    def delete(self):
        user_data = UserRegister.parser.parse_args()
        if not UserModel.find_by_email(user_data['email']):
            return {'message': "Invalid email '{}'".format(user_data['email'])}, 422
        try:
            user_email = UserModel.find_by_email(user_data['email'])
            user_email.delete_from_db()
        except:
                return {'message': "Internal error occurred deleting user"}, 500
        return {'message': 'User deleted successfully'}, 200

# List all users
class UserList(Resource):
    def get(self):
        return {'users': [user.json() for user in UserModel.query.all()]}

    
