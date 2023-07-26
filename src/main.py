import os
import sys

from flask import Flask
from flask import jsonify
import  logging
from api.config.config import (
DevelopmentConfig,
ProductionConfig,
TestingConfig
)
from api.utils.responses import response_with
import api.utils.responses as resp
from  api.config.config import  JWT_SECRET_KEY
from api.utils.database import db

from api.routes.authors import authors_api
from api.routes.books import  books_api
from api.routes.users import  users_api


#for jwt
from flask_jwt_extended import JWTManager

# App initiliazing
app = Flask(__name__)


#Mail config


app.config.update(dict(
    DEBUG = True,
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = 465,
    MAIL_USE_TLS = False,
    # MAIL_PORT = 587,
    MAIL_DEFAULT_SENDER='yaomariussodokin@gmail.com',
    MAIL_USE_SSL = True,
    MAIL_USERNAME = 'yaomariussodokin@gmail.com',
    MAIL_PASSWORD = 'lwubrrlsefquxxlw',
))

key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY4ODY0MjExOSwianRpIjoiZmQ2NGM5N2EtMGQ5Zi00M2U1LTk5NWMtNWI3ZDA5MDlkYjc2IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IlNPRFlBTSIsIm5iZiI6MTY4ODY0MjExOSwiZXhwIjoxNjg4NjQzMDE5fQ.kMmzhcHzoM8xVVEwbXZwIJ7dFKstVecAp4hWwWsTjxw"
# SET the secret key
app.config["JWT_SECRET_KEY"] = JWT_SECRET_KEY

# Registering  routes
app.register_blueprint(authors_api, url_prefix='/api/authors')
app.register_blueprint(books_api, url_prefix='/api/books')
app.register_blueprint(users_api, url_prefix='/api/users')

def get_congig_env():
    if os.environ.get('WORK_ENV') == 'PROD':
        app_config = ProductionConfig
    elif os.environ.get('WORK_ENV') == 'TEST':
        app_config = TestingConfig
    else:
        app_config = DevelopmentConfig
    return  app_config


# Initialising the db
def create_app():
    app_config_env = get_congig_env()
    app.config.from_object(app_config_env)
    db.init_app(app)

    with app.app_context():
        db.create_all()
    return  app

# START GLOBAL HTTP CONFIGURATIONS
@app.after_request
def add_header(response):
    return  response

@app.errorhandler(400)
def bad_request(e):
    logging.error(e)
    return  response_with(resp.BAD_REQUEST_400)


@app.errorhandler(500)
def server_error(e):
    logging.error(e)
    return  response_with((resp.SERVER_ERROR_500))

@app.errorhandler(404)
def not_found(e):
    logging.error(e)
    return  response_with((resp.SERVER_ERROR_404))


db.init_app(app)
with app.app_context():
    db.create_all()


logging.basicConfig(
    stream=sys.stdout,
    format='%(asctime)s|%(levelname)s|%(filename)s:%(lineno)s|%(message)s',
    level=logging.DEBUG
)



# JWT  Auth Initializing
jwt = JWTManager(app)


# Import the mail in utils/emails and initialize it
from api.utils.emails import  mail
mail.init_app(app)

# LAUNCHING APP
if __name__ == '__main__':
    create_app().run(port=5001, use_reloader=False)


