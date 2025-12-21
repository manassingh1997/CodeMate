from django.urls import path
from genai_app.views import RecommendationView

urlpatterns = [
    path('recommendations/', RecommendationView.as_view(), name='recommendations')
]