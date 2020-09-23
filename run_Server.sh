#!/bin/bash

source venv/bin/activate


export FLASK_APP="main.py"
export FLASK_ENV="development"
export APP_SETTINGS_MODULE="config.default"
export CLOUD_STORAGE_BUCKET=apirest-booking-buck

flask run