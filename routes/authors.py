from flask import jsonify, make_response, Blueprint
from models.Author import  Author, AuthorSchema

authors_blueprint = Blueprint('authors', __name__)

@authors_blueprint.route('/authors', methods=['GET'])
def get_all():
    all_authors = Author.query.all()
    author_serializer = AuthorSchema(many=True)
    authors, error = author_serializer.dump(all_authors)
    print("Tous les auteurs ==>", authors)
    return make_response(jsonify({'authors': authors}))

@authors_blueprint.route('/', methods=['GET'])
def hello():
    print("=== Welcome function ====")
    return make_response(jsonify({'hello': "Hello world !!"}))
