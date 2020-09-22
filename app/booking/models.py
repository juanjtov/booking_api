from flask_bcrypt import generate_password_hash, check_password_hash
from flask import Flask,request, jsonify, redirect
from werkzeug.utils import secure_filename

import os
from flask import current_app as app
from google.cloud import storage

CLOUD_STORAGE_BUCKET = os.environ['CLOUD_STORAGE_BUCKET']

class UserLogin():
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')
    
    def check_password(self, password):
        return check_password_hash(self.password, password)

class User(UserLogin):
    def __init__(self, 
    id, 
    name, 
    last_name, 
    email, 
    password, 
    phone_number, 
    address,
    profile_image_url,
    city_id,
    account_type_id,
    lat_location,
    long_location,
    created_at,
    updated_at,
    active):
        self.id = id
        self.name = name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address = address
        self.profile_image_url = profile_image_url
        self.city_id = city_id
        self.account_type_id = account_type_id
        self.lat_location = lat_location
        self.long_location = long_location
        self.created_at = created_at
        self.updated_at = updated_at
        self.active = active
        super().__init__(email, password)

class RoomType():
    def __init__(self, 
    room_type_id,
    room_type_desc):

        self.id = room_type_id
        self.room_type_desc = room_type_desc


class Hotel():
    def __init__(self,
                 name,
                 address,
                 city_id,
                 user_id,
                 description,
                 check_out_hour,
                 rooms_number,
                 hotel_id=None,
                 html_iframe=None,
                 policy=None,
                 created_at=None,
                 updated_at=None,
                 active=None):
        self.name = name
        self.address = address
        self.description = description
        self.city_id = city_id
        self.user_id = user_id
        self.check_out_hour = check_out_hour
        self.rooms_number = rooms_number
        self.hotel_id = hotel_id
        self.html_iframe = html_iframe
        self.policy = policy
        self.created_at = created_at
        self.updated_at = updated_at
        self.active = active

class Files():

    #ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

    # def allowed_file(filename):
	#     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

    def import_images(self, request):
        #Import the images for this hotel 
        #try:
            #This method assumes that the image will be defined as 'hotel_image' within the request.files dictionary
            #If this element is defined then the image is saved and the image file name and URL are extracted
        if request.files:
            #image = request.files['image']
            uploaded_file = request.files.get('image')

             # Create a Cloud Storage client.
            gcs = storage.Client()

            # Get the bucket that the file will be uploaded to.
            bucket = gcs.get_bucket(CLOUD_STORAGE_BUCKET)

            # Create a new blob and upload the file's content.
            blob = bucket.blob(uploaded_file.filename)

            blob.upload_from_string(
            uploaded_file.read(),
            content_type=uploaded_file.content_type
            )       

          
        else:              
            print('no images')

        # The public URL can be used to directly access the uploaded file via HTTP.
        return blob.public_url

        # except KeyError as e:
        #     raise ValidationError('Invalid Hotel: missing ' + e.args[0])

        

class Country():
    def __init__(self,
    country_id, iso, name, spanish_name):
        self.country_id = country_id
        self.iso = iso
        self.name = name
        self.spanish_name = spanish_name

    def serialize(self):
        return {
            'country_id': self.country_id, 
            'iso': self.iso,
            'name': self.name,
            'spanish_name': self.spanish_name
        }

class State():
    def __init__(self, state_id, name, country_id):
        self.state_id = state_id
        self.name = name
        self.country_id = country_id

    def serialize(self):
        return {
            'state_id': self.state_id, 
            'name': self.name,
            'country_id': self.country_id
        }

class City():
    def __init__(self, city_id, name, state_id):
        self.city_id = city_id
        self.name = name
        self.state_id = state_id

    def serialize(self):
        return {
            'city_id': self.city_id, 
            'name': self.name,
            'state_id': self.state_id
        }

class Service():
    def __init__(self, service_id, name, image_url, created_at, updated_at, active, hotel_id, description):
        self.service_id = service_id
        self.name = name
        self.image_url = image_url
        self.created_at = created_at
        self.updated_at = updated_at
        self.active = active
        self.hotel_id = hotel_id
        self.description = description

    def serialize(self):
        return {
            'service_id': self.service_id, 
            'name': self.name,
            'image_url': self.image_url,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'active': self.active,
            'hotel_id': self.hotel_id,
            'description': self.description
        }

class Review():
    def __init__(self, review_id, content, user_id, hotel_id, created_at, updated_at, active):
        self.review_id = review_id
        self.content = content
        self.user_id = user_id
        self.hotel_id = hotel_id
        self.created_at = created_at
        self.updated_at = updated_at
        self.active = active

    def serialize(self):
        return {
            'review_id': self.review_id,
            'content': self.content,
            'user_id': self.user_id,
            'hotel_id': self.hotel_id,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'active': self.active
        }

        
        