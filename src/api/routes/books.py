from ..controllers.books import BookController

from flask import  Blueprint


books_api = Blueprint('books', __name__)

@books_api.route('/', methods = ['POST'])
def store():
    '''store a new books ressource '''
    return  BookController.store()