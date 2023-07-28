from flask import Blueprint

from ..controllers.users import Usercontroller

users_api =  Blueprint('users', __name__)


@users_api.route('/', methods = ['POST','GET'])
def register():
    """
        Create user
        ---
        tags:
            - Users
        parameters:
          - in: body
            name: body
            schema:
              id: UserSignUp
              required:
                - username
                - password
                - email
              properties:
                username:
                  type: string
                  description: Nom d'utilisateur unique de l'utilisateur
                  default: "Sodyam"
                  example: "Sodyam"
                password:
                  type: string
                  description: Mot de passe de l'utilisateur
                  default: "Sodyam@@10"
                  example: "Sodyam@@10"
                email:
                  type: string
                  description: Email de l'utilisateur
                  default: "yaomariussodokin@gmail.com"
                  example: "yaomariussodokin@gmail.com"
        responses:
          201:
            description: Utilisateur créé avec succès
            schema:
              id: UserSignupSchema
              properties:
                code:
                  type: string
          422:
            description: Argument d'entrée invalide
            schema:
              id: InvalidInput
              properties:
                code:
                  type: string
                message:
                  type: string
        """
    return  Usercontroller.register()


@users_api.route('login/', methods = ['POST'])
def login():
    """
    User Login
    ---
    tags:
      - Users
    security:
      - Bearer: []
    parameters:
      - in: body
        name: body
        schema:
          id: UserLogin
          required:
            - password
            - email
          properties:
            email:
              type: string
              description: email de l'utilisateur
              default: "yaomariussodokin@gmail.com"
            password:
              type: string
              description: Mot de passe de l'utilisateur
              default: "S@d/905o"
    responses:
      201:
        description: Utilisateur connecté avec succès
        schema:
          id: UserLoggedIn
          properties:
            code:
              type: string
            message:
              type: string
            value:
              $ref: "#/definitions/UserToken"
      422:
        description: Arguments d'entrée non valides
        schema:
          id: InvalidInput
          properties:
            code:
              type: string
            message:
              type: string
     """
    return  Usercontroller.authenticate_user()

@users_api.route('confirm/<token>', methods = ['GET'])
def verify_email(token):
    """
       User Login
       ---
       tags:
         - Users
       parameters:
         - in: path
           name: token
           schema:
             id: UserVerifyEmail
             required:
               - token
             properties:
               token:
                 type: string
                 description: token generate to the user
                 default: "ggggggggx'855gdffsgdghedeuieoieeç4"

       responses:
         201:
           description: Email_verifier avec succès avec succès
           schema:
             id: UserVerifyEmail
             properties:
               code:
                 type: string
               message:
                 type: string
               value:
                 $ref: "#/definitions/UserToken"
         422:
           description: Arguments d'entrée non valides
           schema:
             id: InvalidInput
             properties:
               code:
                 type: string
               message:
                 type: string
        """
    return  Usercontroller.verify_email(token)