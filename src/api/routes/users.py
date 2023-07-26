from flask import Blueprint

from ..controllers.users import Usercontroller

users_api =  Blueprint('users', __name__)


@users_api.route('/', methods = ['POST','GET'])
def register():
   ''' user register'''
   return  Usercontroller.register()


@users_api.route('login/', methods = ['POST'])
def login():
   ''' login register'''
   return  Usercontroller.authenticate_user()

@users_api.route('confirm/<token>', methods = ['GET'])
def verify_email(token):
   return  Usercontroller.verify_email(token)