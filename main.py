import os

from app.booking.api import create_app


settings_module = os.getenv('APP_SETTINGS_MODULE')
app = create_app(settings_module)
app.config['JWT_SECRET_KEY'] = 't1NP63m4wnBg6nyHYKfmc2TpCOGI4nss'
UPLOAD_FOLDER = "/home/manny/DEVELOPER/MY_PROJECTS/BOOKING_PLATFORM/IMAGES/UPLOADS"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
CLOUD_STORAGE_BUCKET = os.environ['CLOUD_STORAGE_BUCKET']