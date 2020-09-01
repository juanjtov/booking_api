import json
from collections import namedtuple
from json import JSONEncoder


from flask import request, Blueprint, jsonify
from flask_restful import Api, Resource
#from flask_bcrypt import Bcrypt

from ..models import User, UserLogin
from app.common.error_handling import ObjectNotFound
from app.db import set_user, get_user_for_login

booking_app = Blueprint('booking_app', __name__)

api = Api(booking_app)
#bcrypt = Bcrypt(booking_app)

class UserResource(Resource):
    """ API UserResource

    Methods:
        get: HTTP Method
        post: HTTP Methods
    """    
    def get(self):
        user = User(1,
                    'Andres',
                    'Santos', 
                    'ingjuliansantos@gmail.com',
                    '123*',
                    '+573013787020',
                    'Carrera tal con calle x',
                    'img',
                    1125,
                    1,
                    0,0,
                    '','',True)

        login_data = get_user_for_login('ingjulianstos@gmail.com')
        print('\n')
        print(login_data)
        print('\n')

        s = jsonify(user.__dict__)

        return s

    def post(self):
        return {'msg': 'postMethod'}
        
class SignupApi(Resource):
    def post(self):
        post_data = request.get_json()
        data_dict = json.loads(json.dumps(post_data))

        user = User(**data_dict)
        user.hash_password()
        
        print('\nUser: ', user.name)
        
        e = set_user(user)
        return {'id': user.email, 'password': user.password}, 200

class RoomTypeResource(Resource):
    """ API RoomTypeResource

    Methods:
        get: HTTP Method
        post: HTTP Methods
    """  
    def get(self):
        pass

    def post(self):
        pass


api.add_resource(UserResource, '/api/booking/users', endpoint='users_resource')
api.add_resource(RoomTypeResource, '/api/booking/room_type', endpoint='room_type_resource')
api.add_resource(SignupApi, '/api/auth/signup')
