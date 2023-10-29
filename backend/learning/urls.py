from django.urls import path
from . import views

app_name = "learning"

urlpatterns = [
    path("get-closed-ended-questions/", views.LearningGetClosedEndedQuestions.as_view(), name="test"),
]