from django.urls import path
from . import views

app_name = "learning"

urlpatterns = [
    path("get-closed-ended-questions/", views.LearningGetClosedEndedQuestions.as_view(), name="learning_cloded_ended_questions"),
    path("test/", views.Test.as_view()),
]