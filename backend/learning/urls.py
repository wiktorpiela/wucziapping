from django.urls import path
from . import views

app_name = "learning"

urlpatterns = [
    path("get-closed-ended-questions/", views.LearningGetClosedEndedQuestions.as_view(), name="learning_cloded_ended_questions"),
    path("get-question-types/", views.QuestionTypesDifficultyLevel.as_view(), name="question_types"),
]