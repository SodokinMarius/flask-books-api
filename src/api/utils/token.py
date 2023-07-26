from itsdangerous import  URLSafeTimedSerializer
from flask import current_app

from ..config.config import  MAIL_CONF, SECRET_VALUES
def generate_verification_token(email):
    # serializer = URLSafeTimedSerializer(current_app.config.get('SECRET_KEY'))
    serializer = URLSafeTimedSerializer(SECRET_VALUES.get('SECRET_KEY'))

    # return  serializer.dump(email, salt=current_app.get('SECURITY_PASSWORD_SALT'))
    return  serializer.dumps(email, salt=SECRET_VALUES.get('SECURITY_PASSWORD_SALT'))

def confirm_verification_token(token, expiration=3600):
    # serializer = URLSafeTimedSerializer(current_app.config.get('SECRET_KEY'))
    serializer = URLSafeTimedSerializer(SECRET_VALUES.get('SECRET_KEY'))
    try :
        email = serializer.loads(
            token,
            # salt=current_app.config.get('SECURITY_PASSWORD_SALT'),
            salt=SECRET_VALUES.get('SECURITY_PASSWORD_SALT'),
            max_age=expiration
        )
    except Exception as e:
        return e
    return  email