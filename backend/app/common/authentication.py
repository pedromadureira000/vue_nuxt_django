import jwt, datetime
from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication 
from app import settings
from app.core.models import User

class JWTAuthentication(BaseAuthentication):

    def authenticate(self, request):
        is_ambassador = 'api/ambassador' in request.path

        token =request.COOKIES.get('jwt')

        if not token:
            return None
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed('User not Found!') 

        if (is_ambassador and payload['scope'] != 'ambassador') or (not is_ambassador and payload['scope'] != 'admin'):
            raise exceptions.AuthenticationFailed('Invalid Scope!')

        user = User.objects.get(pk=payload['user_id'])

        if user is None:
            raise exceptions.AuthenticationFailed('User not found')

        return (user, None) #if send just user in response, will get an error "cannot unpack non-iterable User object"

    @staticmethod
    def generate_jwt(id, scope):
        payload = {
            'user_id': id,
            'scope': scope,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1), #expiration
            'iat': datetime.datetime.utcnow(), # creation date
        }

        return jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')


