from ..utils.database import  db
from marshmallow import  fields

from  flask_marshmallow import Schema as ModelSchema

from passlib.hash import pbkdf2_sha256 as sha256


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), unique = True, nullable = False)
    password = db.Column(db.String(255), nullable = False)
    email = db.Column(db.String(125), unique = True, nullable = False)
    is_verified = db.Column(db.Boolean, default = False, nullable = False)

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    @classmethod
    def find_by_username(cls,username:str):
        return  cls.query.filter_by(username = username).first()

    @classmethod
    def find_by_email(cls, email: str):
        return cls.query.filter_by(email=email).first()

    @staticmethod
    def generate_hash(password):
        return  sha256.hash(password)

    @staticmethod
    def verify_hash(password, hash):
        return  sha256.verify(password,hash)


class UserSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = User
        sqla = db.session
    id = fields.Number(dump_only=True)
    username = fields.String(required=True)
    password = fields.String(required=True)
    email = fields.String(required=True)


