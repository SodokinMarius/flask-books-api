from flask import Blueprint
from ..controllers.authors import AuthorController

from flask_jwt_extended import jwt_required


# let's configure the Blueprint
authors_api = Blueprint('authors', __name__)

@authors_api.route('/avatar/<filename>', methods=['POST']) # this might be  @app.route
def render_uploaded_file(filename):
    return  AuthorController.render_file(filename)


@authors_api.route('/', methods=['POST'])
@jwt_required()
def register_author():
    """
           Create  author
           ---
           tags:
             - Author
           parameters:
             - in: body
               name: body
               schema:
                 id: Author
                 required:
                   - first_name
                   - last_name
                   - books
                 properties:
                   first_name:
                     type: string
                     description: The first name of the author
                     default: "Yao Marius"
                     example: "Yao Marius"
                   last_name:
                     type: string
                     description: The Last name of the author
                     default: "Sodokin"
                     example: "Sodokin"
                   books:
                     type: array
                     default: []
             - in: header
               name : authorization
               type: string
               required: true
           security:
              - Bearer: []
           responses:
             200:
               description: Author created successfully
               schema:
                 id: AuthorCreated
                 properties:
                   code:
                     type: string
                   message:
                     type: string
                   value:
                      schema:
                        id: AuthorFull
                        properties:
                            first_name:
                                type: string
                            last_name:
                                type: string
                            books:
                                type: array
                                items:
                                    schema:
                                        id: BookSchema

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

    return AuthorController.register_author()

@authors_api.route('/avatar/<int:author_id>', methods=['POST'])
@jwt_required()
def upload_author_avatar(author_id:int):
    """
       Upsert  author avatar
       ---
       tags:
             - Author
       parameters:
         - in: body
           name: body
           schema:
             id: Author
             required:
               - avatar
             properties:
               avatar:
                 type: file
                 description: upload Image file
         - name: author_id
           in: path
           description: ID of the author
           required: true
           schema:
              type: string
       responses:
         200:
           description: Author avatar upserted successfully
           schema:
             id: AuthorCreated
             properties:
               code:
                 type: string
               message:
                 type: string
               value:
                  schema:
                    id: AuthorFull
                    properties:
                        first_name:
                            type: string
                        last_name:
                            type: string
                        books:
                            type: array
                            items:
                                schema:
                                    id: BookSchema

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
    print("Voilà ====>", author_id)
    return AuthorController.upload_author_avatar(author_id)


@authors_api.route('/', methods = ['GET'])
@jwt_required()
def get_all_authors():
    """
    Get authors
    ---
    tags:
      - Author
    security:
      - Bearer: []
    parameters:
      - in: header
        name: authorization
        type: string
        required: true
    responses:
      200:
        description: Auteurs récupérés avec succès
        schema:
          id: AuthorRetrieved
          properties:
            code:
              type: string
            message:
              type: string
            value:
              $ref: "#/definitions/AuthorFull"
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
    return AuthorController.get_all_authors()


@authors_api.route('/<int:id>', methods = ['GET'])
@jwt_required()
def get_by_id_(id):
    """
       Get a specific author
       ---
       tags:
         - Author
       security:
         - Bearer: []
       parameters:
         - in: path
           name : id
           type: integer
           required: true
         - in: header
           name: authorization
           type: string
           required: true
       responses:
         200:
           description: Auteur récupéré avec succès
           schema:
             id: AuthorRetrieved
             properties:
               code:
                 type: string
               message:
                 type: string
               value:
                 $ref: "#/definitions/AuthorFull"
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
    return  AuthorController.get_by_id(id)


@authors_api.route('/<int:id>', methods = ['PUT'])
@jwt_required()
def update(id):
    """
       Update  author
       ---
       tags:
         - Author
       parameters:
         - in: path
           name : id
           type: integer
           required: true
         - in: body
           name: body
           schema:
             id: Author
             required:
               - first_name
               - last_name
               - books
             properties:
               first_name:
                 type: string
                 description: The first name of the author
                 default: "Yao Marius"
                 example: "Yao Marius"
               last_name:
                 type: string
                 description: The Last name of the author
                 default: "Sodokin"
                 example: "Sodokin"
               books:
                 type: array
                 default: []
         - in: header
           name : authorization
           type: string
           required: true
       security:
          - Bearer: []
       responses:
         200:
           description: Author updated successfully
           schema:
             id: AuthorUpdated
             properties:
               code:
                 type: string
               message:
                 type: string
               value:
                  schema:
                    id: AuthorPut
                    properties:
                        first_name:
                            type: string
                        last_name:
                            type: string
                        books:
                            type: array
                            items:
                                schema:
                                    id: BookSchema

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
    return  AuthorController.update(id)


@authors_api.route('/<int:id>', methods = ['PATCH'])
@jwt_required()
def patch(id):
    """
           Update   author fields
           ---
           tags:
             - Author
           parameters:
             - in: path
               name : id
               type: integer
               required: true
             - in: body
               name: body
               schema:
                 id: Author
                 required:
                   - first_name
                   - last_name
                   - books
                 properties:
                   first_name:
                     type: string
                     description: The first name of the author
                     default: "Yao Marius"
                     example: "Yao Marius"
                   last_name:
                     type: string
                     description: The Last name of the author
                     default: "Sodokin"
                     example: "Sodokin"
                   books:
                     type: array
                     default: []
             - in: header
               name : authorization
               type: string
               required: true
           security:
              - Bearer: []
           responses:
             200:
               description: Author updated successfully
               schema:
                 id: AuthorUpdated
                 properties:
                   code:
                     type: string
                   message:
                     type: string
                   value:
                      schema:
                        id: AuthorPatch
                        properties:
                            first_name:
                                type: string
                            last_name:
                                type: string
                            books:
                                type: array
                                items:
                                    schema:
                                        id: BookSchema

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
    return  AuthorController.patch(id)

@authors_api.route('/<int:id>', methods = ['DELETE'])
@jwt_required()
def delete(id):
    """
           Delete a specific author
           ---
           tags:
             - Author
           security:
             - Bearer: []
           parameters:
             - in: path
               name : id
               type: integer
               required: true
             - in: header
               name: authorization
               type: string
               required: true
           responses:
             200:
               description: Auteur supprimé avec succès
               schema:
                 id: AuthorDeleted
                 properties:
                   first_name:
                     type: string
                   last_name:
                     type: string
                   value:
                     $ref: "#/definitions/AuthorFull"
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
    return  AuthorController.delete(id)


