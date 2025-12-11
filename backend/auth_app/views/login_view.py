from rest_framework import APIView
from rest_framework.response import Response
from auth_app.serializers.login_serializer import LoginSerializer
from auth_app.context.auth_context import AuthContext

class LoginView(APIView):

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        #defualt strategy is email password

        auth_type = request.data.get('type', 'email')

        try:
            tokens = AuthContext.authenticate(auth_type, serializer.validated_date)
        except ValueError as e:
            return Response({'error': str(e)}, status=400)
        
        if not tokens:
            return Response({'error': 'Invalid credentials'}, status=401)
        
        return Response(tokens)