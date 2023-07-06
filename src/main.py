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

from api.utils.database import db

from api.routes.authors import authors_api
from api.routes.books import  books_api

app = Flask(__name__)


# Registering the author routes
app.register_blueprint(authors_api, url_prefix='/api/authors')
app.register_blueprint(books_api, url_prefix='/api/books')

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


if __name__ == '__main__':
    create_app().run(port=5001, use_reloader=False)