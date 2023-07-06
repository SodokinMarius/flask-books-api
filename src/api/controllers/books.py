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

    @classmethod
    def get_all(cls):
        books_query = Book.query.all()
        book_serializer = BookSchema(many=True, only=['id', 'title', 'year', 'author_id'])
        books = book_serializer.dump(books_query)
        return response_with(resp.SUCCESS_200, value={
            "data": books
        })

    @classmethod
    def get_by_id(cls, id: int):
        book_query = Book.query.get_or_404(id)
        book_serializer = BookSchema()
        book = book_serializer.dump(book_query)
        return response_with(resp.SUCCESS_200, value={
            "data": book
        })

    @classmethod
    def update(cls, id: int):
        data: dict = request.get_json()
        book = Book.query.get_or_404(id)
        if data.get('title'):
            book.title = data.get('title')

        if data.get('year'):
            book.year = data.get('year')

        if data.get('author_id'):
            book.author_id = data.get('author_id')

        db.session.add(book)
        db.session.commit()

        book_serializer = BookSchema(only=['id', 'title', 'year','author_id'])
        updated_book = book_serializer.dump(book)
        return response_with(resp.SUCCESS_200, value={
            "data": updated_book
        })

    @classmethod
    def patch(cls, id: int):
        data: dict = request.get_json()
        book = Book.query.get_or_404(id)

        book.title = data.get('title')
        book.year = data.get('year')
        book.author_id = data.get('author_id')

        db.session.add(book)
        db.session.commit()

        book_serializer = BookSchema(only=['id', 'title', 'year', 'author_id'])
        updated_book = book_serializer.dump(book)
        return response_with(resp.SUCCESS_200, value={
            "data": updated_book
        })

    @classmethod
    def delete(cls, id: int):
        book = Book.query.get_or_404(id)
        db.session.delete(book)
        db.session.commit()
        return response_with(resp.SUCCESS_200)


