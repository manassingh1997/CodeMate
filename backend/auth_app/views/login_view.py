from rest_framework.views import APIView
from rest_framework.response import Response
from auth_app.serializers.login_serializer import LoginSerializer
from auth_app.context.auth_context import AuthContext

class LoginView(APIView):
    

    authentication_classes = []  # Login does NOT require auth
    permission_classes = []

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # default strategy: email/password
        auth_type = "email"

        try:
            tokens = AuthContext.authenticate(auth_type, serializer.validated_data)
        except ValueError as e:
            return Response({"error": str(e)}, status=400)

        if not tokens:
            return Response({"error": "Invalid credentials"}, status=401)

        return Response(tokens)
