from django.urls import path
from users_app.views import MeView

urlpatterns = [
    path('me/', MeView.as_view(), name='users-me'),
]