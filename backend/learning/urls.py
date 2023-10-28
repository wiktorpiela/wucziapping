from django.urls import path
from . import views

app_name = "learning"

urlpatterns = [
    path("test-view/", views.Test.as_view(), name="test"),
]