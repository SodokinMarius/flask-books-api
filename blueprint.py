from routes.authors import authors_blueprint
from app import app

app.register_blueprint(authors_blueprint)
