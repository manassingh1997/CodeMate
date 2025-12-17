from django.urls import path
from coding_logs.views import CodingLogCreateView

urlpatterns = [
    path('log/', CodingLogCreateView.as_view()),
]