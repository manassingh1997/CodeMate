from django.contrib.auth import authenticate
from auth_app.strategies.base import AuthStrategy
from auth_app.services.jwt_service import JWTService

class EmailPasswordStrategy(AuthStrategy):
    def authenticate(self, data):
        email = data.get('email')
        password = data.get('password')

        user = authenticate(email=email, password=password)
        if not user:
            return None
        return JWTService.generate_token(user)
    