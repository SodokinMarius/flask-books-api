from flask import Blueprint

from ..controllers.authors import AuthorController

# let's configure the Blueprint
authors_api = Blueprint('authors', __name__)


@authors_api.route('/', methods=['POST'])
def register_author():
    '''register an author'''
    return AuthorController.register_author()

@authors_api.route('/', methods = ['GET'])
def get_all_authors():
    'retrieve all author'
    return  AuthorController.get_all_authors()

@authors_api.route('/<int:id>', methods = ['GET'])
def get_by_id_(id):
    'get here author by id'
    return  AuthorController.get_by_id(id)


@authors_api.route('/<int:id>', methods = ['PUT'])
def update(id):
    '''update author'''
    return  AuthorController.update(id)


@authors_api.route('/<int:id>', methods = ['PATCH'])
def patch(id):
    '''patch author'''
    return  AuthorController.patch(id)

@authors_api.route('/<int:id>', methods = ['DELETE'])
def delete(id):
    '''Delete author by his id'''
    return  AuthorController.delete(id)


