from rest_framework.views import APIView
from rest_framework.response import Response
from auth_app.serializers.register_serializer import RegisterSerializer
from auth_app.services.jwt_service import JWTService


class RegisterView(APIView):

    authentication_classes = []  # Registration does NOT require auth
    permission_classes = []

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)  # <-- FIXED TYPO

        user = serializer.save()
        tokens = JWTService.generate_token(user)

        return Response({
            "message": "User registered successfully",
            "tokens": tokens
        }, status=201)