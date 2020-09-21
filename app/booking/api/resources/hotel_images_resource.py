
from flask import Flask, request, jsonify
from flask_restful import Resource
from app.booking.models import Files


class UploadImages(Resource):

    def post(self):

        new_image = Files()
        test = new_image.import_images(request)

        # post_data = request.get_json()
        # data_dict = json.loads(json.dumps(post_data))

        # user = User(**data_dict)
        # user.hash_password()
        
        # e = set_user(user)
        


        return test


