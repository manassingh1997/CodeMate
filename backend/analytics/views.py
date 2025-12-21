from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from analytics.services.coding_analytics import get_user_coding_analytics
# Create your views here.

class AnalyticsSummaryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = get_user_coding_analytics(request.user)
        return Response(data)