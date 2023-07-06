from ..routes.authors import authors_api

from ...main import app
# Registering the author routes
with app.app_context():
    app.register_blueprint(authors_api, url_prefix='/api/authors')
