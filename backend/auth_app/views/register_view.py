from rest_framework.views import APIView
from rest_framework.response import Response
from auth_app.serializers.register_serializer import RegisterSerializer
from auth_app.services.jwt_service import JWTService


class RegisterView(APIView):

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valide(raise_exception=True)

        user = serializer.save()
        tokens = JWTService.generate_tokens(user)

        return Response({
            "message": "User registered successfully",
            "tokens": tokens
        }, status=201)