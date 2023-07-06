from ..utils.responses import response_with
from ..utils import  responses as resp

from ..models.users import User, UserSchema
from ..utils.database import db
from flask import  request
from flask_jwt_extended import create_access_token, create_refresh_token



class Usercontroller:
    
    @classmethod
    def register(cls):
        try:
            data : dict = request.get_json()

            # password crypting
            data.update({
                "password": User.generate_hash(data.get('password'))
            })

            if User.find_by_username(data.get('username')):
                return response_with(resp.BAD_REQUEST_400_RESSOURCE_EXISTS)

            user_serializer = UserSchema()
            user = user_serializer.load(data)
            user = User(**user)
            user.create()  # Create the author ressource
            response = user_serializer.dump(user)
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
    def authenticate_user(cls):
        # try:
            data : dict = request.get_json()
            current_user = User.find_by_username(data.get('username'))

            if not current_user :
                return  response_with(resp.SERVER_ERROR_404)

            if User.verify_hash(data.get('password'), current_user.password):
                access_token = create_access_token(identity= data.get('username'))
                refresh_token = create_refresh_token(identity= data.get('username'))

                return response_with(
                    resp.SUCCESS_201,
                    value= {
                        "message": "Logged as {}".format(data.get('username')),
                        "access_token" : access_token,
                        "refresh_token" : refresh_token
                    }
                )
            else:
                return  response_with(resp.UNAUTHORIZED_403)
        # except Exception as e:
        #     print(e)
        #     return  response_with(resp.INVALID_INPUT_422)






        

