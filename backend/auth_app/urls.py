from django.urls import path
from auth_app.views.register_view import RegisterView
from auth_app.views.login_view import LoginView


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),  
]