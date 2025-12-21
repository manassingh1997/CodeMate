from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from genai_app.services.recommendation_engine import get_ai_recommendations
# Create your views here.

class RecommendationView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        result = get_ai_recommendations(request.user)
        return Response({
            "recommendations": result
        })
