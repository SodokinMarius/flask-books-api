from ..utils.database import  db
from ..utils.responses import response_with
from ..utils import  responses as resp

from ..models.books import Book, BookSchema
from ..utils.database import db
from flask import  request
from flask import  make_response,jsonify

class BookController:


    @classmethod
    def store(cls):
        try:
            data = request.get_json()
            print('Initial data',data)
            book_serializer = BookSchema()
            book = book_serializer.load(data)
            book = Book(**book)
            book.create()  # Create the author ressource
            response = book_serializer.dump(book)
            print("La reponse " ,response)
            return response_with(resp.SUCCESS_201,
                                 value={
                                 "data":response

                             })
        except Exception as e:
            print("Suite",e)
            val =  response_with(resp.INVALID_INPUT_422)
            print('Retour',val)
            return val


