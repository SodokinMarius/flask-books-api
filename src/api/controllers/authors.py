from ..utils.database import  db
from ..utils.responses import response_with
from ..utils import  responses as resp

from ..models.authors import Author,AuthorSchema
from ..utils.database import db
from flask import  request
from flask import  make_response,jsonify
class AuthorController:

    @classmethod
    def register_author(cls):
        try:
            data = request.get_json()
            print('Initial data',data)
            author_serializer = AuthorSchema()
            author = author_serializer.load(data)
            author = Author(**author)
            author.create()  # Create the author ressource
            response = author_serializer.dump(author)
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
    def get_all_authors(cls):
        authors_query = Author.query.all()
        author_serializer = AuthorSchema(many=True, only=['id','last_name','first_name','books'])
        authors = author_serializer.dump(authors_query)
        return  response_with(resp.SUCCESS_200, value={
            "data" : authors
        })

    @classmethod
    def get_by_id(cls, id:int):
        author_query = Author.query.get_or_404(id)
        author_serializer = AuthorSchema()
        author = author_serializer.dump(author_query)
        return response_with(resp.SUCCESS_200, value={
            "data": author
        })

    @classmethod
    def update(cls,id:int):
        data : dict = request.get_json()
        author = Author.query.get_or_404(id)
        if data.get('first_name') :
            author.first_name = data.get('first_name')

        if data.get('last_name'):
            author.last_name = data.get('last_name')

        db.session.add(author)
        db.session.commit()

        author_serializer = AuthorSchema(only=['id','first_name','last_name'])
        update_author = author_serializer.dump(author)
        return response_with(resp.SUCCESS_200, value={
            "data":update_author
        })

# TOTO : Code duplicate hier
    @classmethod
    def patch(cls, id:int):
        data: dict = request.get_json()
        author = Author.query.get_or_404(id)
        if data.get('first_name'):
            author.first_name = data.get('first_name')

        if data.get('last_name'):
            author.last_name = data.get('last_name')

        db.session.add(author)
        db.session.commit()

        author_serializer = AuthorSchema(only=['id', 'first_name', 'last_name'])
        update_author = author_serializer.dump(author)
        return response_with(resp.SUCCESS_200, value={
            "data": update_author
        })


    @classmethod
    def delete(cls, id:int):
        author = Author.query.get_or_404(id)
        db.session.delete(author)
        db.session.commit()
        return response_with(resp.SUCCESS_200)






