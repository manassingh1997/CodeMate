from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from users_app.models import UserProfile
from users_app.serializers import UserProfileSerializer

from users_app.services.profile_scraper import update_profile_stats
# Create your views here.

class MeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        profile, _ = UserProfile.objects.get_or_create(user=request.user)
        update_profile_stats(profile)
        serializer = UserProfileSerializer(profile)
        return Response(serializer.data)
    
    def patch(self, request):
        profile, _ = UserProfile.objects.get_or_create(user=request.user)
        update_profile_stats(profile)
        serializer = UserProfileSerializer(
            profile,
            data=request.data,
            partial=True,
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    

