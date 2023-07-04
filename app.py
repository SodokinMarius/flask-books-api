from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import  SQLALCHEMY_DATABASE_URI, SQLITE_URI
from flask_marshmallow import Schema as ModelSchema
from marshmallow import fields
from flask import jsonify, make_response, Blueprint, request

from marshmallow import ValidationError


############################## CONFIGURATIONS #############################
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI

print("Db ", app.config['SQLALCHEMY_DATABASE_URI'] )
db = SQLAlchemy(app)


############################## MODELS #############################
class Author(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(255),nullable=False)
    specialisation = db.Column(db.String(255),nullable=False)

    def __init__(self,name, specialisation):
        self.name = name
        self.specialisation = specialisation

    __tablename__ = 'authors'

    def __repr__(self):
        return  f'{self.name} - {self.specialisation}'

    def __repr__(self):
        return f' Author {self.id} - {self.name} -  {self.specialisation}'

    # Create and return an author
    def create(self):
        db.session.add(self)
        db.session.commit()
        return  self

db.create_all()

class AuthorSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model =  Author
        sqla_session = db.session
    id = fields.Number(dump_only=True)
    name = fields.String(required=True)
    specialisation = fields.String(required=True)




















#################### ROUTES ############################"
@app.route('/hello', methods=['GET'])
def hello():
    print("=== Welcome function ====")
    return jsonify({'hello': "Hello world !!"})


@app.route('/authors', methods=['GET'])
def get_all():
    all_authors = Author.query.all()
    author_serializer = AuthorSchema(many=True)
    if not all_authors:
        return make_response(jsonify({'message': 'Not Author registered !'}))

    authors = author_serializer.dump(all_authors)

    print("Tous les auteurs ==>", authors)
    return make_response(jsonify({'authors': authors}))


@app.route('/authors', methods = ['POST'])
def create_author():

    data = request.get_json()
    author_serializer = AuthorSchema()

    try:
        author = author_serializer.load(data)
        author_instance = Author(**author)
        # db.session.add(author_instance)
        # db.session.commit()
        author_instance.create()
        response = author_serializer.dump(author_instance)
        return make_response(jsonify({
            'data': response,
            'message': 'Created successfully!'
        }), 201)
    except ValidationError as e:
        return make_response(jsonify({
            'message': 'Invalid data',
            'errors': e.messages,
        }), 400)


@app.route('/authors/<int:id>', methods = ['GET'])
def get_author_by_id(id):
     author = Author.query.get(id)
     if not author:
         return  make_response(jsonify({
             "ERROR" : "Author not found !"
         }))
     author_serializer = AuthorSchema()
     serialized_author = author_serializer.dump(author)
     return make_response(jsonify({
         "author": serialized_author
     }))

@app.route('/authors/<int:id>', methods = ['PUT'])
def update_author(id):
    data = request.get_json()
    author = Author.query.get(id)
    if not author:
        return make_response(jsonify({
            "ERROR": "Author not found !"
        }))

    if data.get('name'):
        author.name = data.get('name')

    if data.get('specialisation'):
        author.specialisation = data.get('specialisation')

    db.session.add(author)
    db.session.commit()

    author_serializer = AuthorSchema(only=[
        'id',
        'name',
        'specialisation'
    ])

    serialized_author = author_serializer.dump(author)
    return make_response(jsonify({
        "author": serialized_author
    }))


@app.route('/authors/<int:id>', methods = ['DELETE'])
def delete(id):
    author = Author.query.get(id)

    if not author:
        return  make_response(jsonify(
            {
            "ERROR" : "Author not found"
            }
        ))

    db.session.delete(author)
    db.session.commit()
    return make_response(jsonify(
        {
            "message": "Author  Deleted successfully !"
        }
    ))














###############################" APP LAUNCHING ###########################
if __name__ == '__main__':
    db.create_all()  # Créez les tables dans la base de données avant de lancer l'application
    print("All migrations done successfully !")
    app.run(debug=True, port=5001)
