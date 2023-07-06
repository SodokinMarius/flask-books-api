# from api.utils.database import db
from ..utils.database import  db
from marshmallow import Schema as ModelSchema

from marshmallow import fields

from ..models.books import  BookSchema
class Author(db.Model):

    __tablename__ = 'authors'
    id = db.Column(db.Integer,primary_key=True, autoincrement = True)
    first_name = db.Column(db.String(255),nullable=False)
    last_name = db.Column(db.String(255),nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    books = db.relationship('Book',backref='authors', cascade = 'all , delete-orphan', uselist=True)


    def __init__(self,first_name, last_name, books=[]):
        self.first_name = first_name
        self.last_name = last_name
        self.books = books

    def __repr__(self):
        return  f'{self.first_name} - {self.last_name}'

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self
class AuthorSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model =  Author
        sqla_session = db.session
    id = fields.Number(dump_only=True)
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)
    created =  fields.String(dump_only=True)
    books = fields.Nested(BookSchema,many=True,
                          only=['title','year','id'])