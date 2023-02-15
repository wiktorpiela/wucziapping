from django.urls import path
from . import views

app_name = "quiz"

urlpatterns = [
    path("", views.home, name="home"),
    path("quiz-questions/", views.quiz_questions, name="quiz_questions"),
]