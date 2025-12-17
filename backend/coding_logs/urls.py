from django.urls import path
from coding_logs.views import CodingLogCreateView, CodingLogListView

urlpatterns = [
    path('log/', CodingLogCreateView.as_view(), name="coding-log-create"),
    path('list/', CodingLogListView.as_view(), name="coding-log-list"),
]