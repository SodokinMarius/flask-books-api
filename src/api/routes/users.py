from flask import Blueprint

from ..controllers.users import Usercontroller

users_api =  Blueprint('users', __name__)


@users_api.route('/', methods = ['POST'])
def register():
   ''' user register'''
   return  Usercontroller.register()


@users_api.route('login/', methods = ['POST'])
def login():
   ''' login register'''
   return  Usercontroller.authenticate_user()