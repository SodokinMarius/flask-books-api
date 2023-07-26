from ..controllers.books import BookController

from flask import  Blueprint

from flask_jwt_extended import  jwt_required
books_api = Blueprint('books', __name__)

@books_api.route('/', methods = ['POST'])
@jwt_required()
def store():
    '''store a new books ressource '''
    return  BookController.store()


@books_api.route('/', methods = ['GET'])
@jwt_required()
def get_all():
    '''get all books '''
    return  BookController.get_all()


@books_api.route('/<int:id>', methods = ['GET'])
@jwt_required()
def get_by_id_(id):
    'get here book by id'
    return  BookController.get_by_id(id)


@books_api.route('/<int:id>', methods = ['PUT'])
@jwt_required()
def update(id):
    '''update book'''
    return  BookController.update(id)


@books_api.route('/<int:id>', methods = ['PATCH'])
@jwt_required()
def patch(id):
    '''patch book'''
    return  BookController.patch(id)


@books_api.route('/<int:id>', methods = ['DELETE'])
@jwt_required()
def delete(id):
    '''Delete book by his id'''
    return  BookController.delete(id)