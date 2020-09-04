import json
import datetime

from collections import namedtuple
from json import JSONEncoder

from flask import request, Blueprint, jsonify
from flask_restful import Api, Resource


from flask import Response, request
from flask_jwt_extended import create_access_token, jwt_required

from ..models import User, UserLogin
from app.common.error_handling import ObjectNotFound
from app.db import set_user, get_user_for_login, get_user

from flask import current_app

booking_app = Blueprint('booking_app', __name__)


api = Api(booking_app)


class UserResource(Resource):
    """ API UserResource

    Methods:
        get: HTTP Method
        post: HTTP Methods
    """
    @jwt_required    
    def get(self):
        user = User(1,
                    'Andres',
                    'Santos', 
                    'asdasd@gmail.com',
                    '123*',
                    '+573013787020',
                    'Carrera tal con calle x',
                    'img',
                    1125,
                    1,
                    0,0,
                    '','',True)

        s = jsonify(user.__dict__)

        return s
    
    @jwt_required
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

class LoginApi(Resource):
    def post(self):
        body = request.get_json()
        user_dict = get_user(body.get('email'))[0]
      
        user = User(**user_dict)
        authorized = user.check_password(body.get('password'))
        if not authorized:
            return {'error': 'Email or password invalid'}, 401

        expires = datetime.timedelta(days=7)
        access_token = create_access_token(identity=str(user.id), expires_delta=expires)

        return {'token': access_token}, 200
class RoomTypeResource(Resource):
    """ API RoomTypeResource

    Methods:
        get: HTTP Method
        post: HTTP Methods
    """
    @jwt_required  
    def get(self):
        pass

    @jwt_required
    def post(self):
        pass


api.add_resource(UserResource, '/api/booking/users', endpoint='users_resource')
api.add_resource(RoomTypeResource, '/api/booking/room_type', endpoint='room_type_resource')
api.add_resource(SignupApi, '/api/auth/signup')
api.add_resource(LoginApi, '/api/auth/login')
