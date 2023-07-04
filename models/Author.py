from app import  db
from flask_marshmallow import Schema as ModelSchema
from marshmallow import fields

class Author(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(255),nullable=False)
    specialisation = db.Column(db.String(255),nullable=False)

    def __init__(self,name, specialisation):
        self.name = name
        self.specialisation = specialisation

    def __repr__(self):
        return  f'{self.name} - {self.specialisation}'


class AuthorSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model =  Author
        sqla_session = db.session
    id = fields.Number(dump_only=True)
    name = fields.String(required=True)
    specialisation = fields.String(required=True)

