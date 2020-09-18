import os

from app.booking.api import create_app


settings_module = os.getenv('APP_SETTINGS_MODULE')
app = create_app(settings_module)
app.config['JWT_SECRET_KEY'] = 't1NP63m4wnBg6nyHYKfmc2TpCOGI4nss'

if __name__ == "__main__":
    app.run(host='0.0.0.0')
    