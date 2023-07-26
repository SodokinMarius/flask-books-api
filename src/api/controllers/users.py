from ..utils.responses import response_with
from ..utils import  responses as resp

from ..models.users import User, UserSchema
from ..utils.database import db
from flask import  request
from flask_jwt_extended import create_access_token, create_refresh_token

from ..utils.token import (
    generate_verification_token,
    confirm_verification_token
)


# for cua
from ..utils.emails import  send_email
from flask import  url_for, render_template_string

class Usercontroller:
    
    @classmethod
    def register(cls):
        # try:
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


            # generate email token
            token = generate_verification_token(data.get('email'))
            verification_email = url_for('users.verify_email', token=token, _external=True)

            # generate verification template
            html = render_template_string(
                "<p>Welcome ! Thanks you for signing up. PLease, follow this link bellow to activate your account : </p>"
                "<p><a href='{{verification_email}}'>{{verification_email}}</a></p><br><p>Thanks you !!</p>",
            verification_email=verification_email
            )

            subject= "Account Email Verification"
            #Send the mail
            send_email(user.email,subject,html)

            # ======== End =======

            response = user_serializer.dump(user)
            print("La reponse " ,response)
            return response_with(resp.SUCCESS_201,
                                 value={
                                 "data":response

                             })
        # except Exception as e:
        #     print("Suite",e)
        #     val =  response_with(resp.INVALID_INPUT_422)
        #     print('Retour',val)
        #     return val

    @classmethod
    def authenticate_user(cls):
        try:
            data : dict = request.get_json()
            current_user = None
            if data.get('email'):
                current_user = User.find_by_email(data.get('email'))
            elif data.get('username'):
                current_user = User.find_by_username(data.get('username'))

            if not current_user :
                return  response_with(resp.SERVER_ERROR_404)

            '''Verifions si le mail exists et est verifié'''
            if current_user and not  current_user.is_verified:
                return  response_with(resp.BAD_REQUEST_400)

            if User.verify_hash(data.get('password'), current_user.password):
                access_token = create_access_token(identity= current_user.username)
                refresh_token = create_refresh_token(identity= current_user.username)

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
        except Exception as e:
            print(e)
            return  response_with(resp.INVALID_INPUT_422)


    @classmethod
    def verify_email(cls,token):
        try :
            email = confirm_verification_token(token)
        except Exception as e:
            return response_with(resp.SERVER_ERROR_500)

        # Check the user matched to the retrieved email
        user = User.query.filter_by(email=email).first_or_404()

        if user.is_verified:
            return  response_with(resp.INVALID_INPUT_422)
        else:
            user.is_verified = True
            db.session.add(user)
            db.session.commit()
            return  response_with(resp.SUCCESS_200,
                                  value={
                                      "message":"Email verified successfully ! You can process to login now !!"
                                  })





        

