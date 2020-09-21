
from flask import Blueprint
from flask_restful import Api
from flask_cors import CORS
from .resources.user_resource import UserResource
from .resources.auth_resource import SignupApi, LoginApi
from .resources.room_type_resource import RoomTypeResource
from .resources.hotel_resource import HotelResource
from .resources.places_resource import PlacesResource
from .resources.hotel_images_resource import UploadImages
from .resources.services_resource import ServicesResource
from .resources.reviews_resource import ReviewsResource

booking_app = Blueprint('booking_app', __name__)

api = Api(booking_app)
cors = CORS(booking_app, resources={r"/api/*": {"origins": "*"}})


api.add_resource(UserResource, '/api/booking/users')
api.add_resource(RoomTypeResource, '/api/booking/room_type')
api.add_resource(SignupApi, '/api/auth/signup')
api.add_resource(LoginApi, '/api/auth/login')
api.add_resource(HotelResource, '/api/booking/hotels')
api.add_resource(ServicesResource, '/api/booking/services')
api.add_resource(ReviewsResource, '/api/booking/reviews')
api.add_resource(PlacesResource, '/api/booking/places', '/api/booking/places/<string:place_type>')
api.add_resource(UploadImages, '/api/booking/files')
