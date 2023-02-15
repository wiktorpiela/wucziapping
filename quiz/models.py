from django.db import models

class QuizQuestionsAbcd(models.Model):
    type = models.CharField(max_length=100)
    question = models.CharField(max_length=500)
    suffix = models.CharField(max_length=100)
    ans1 = models.CharField(max_length=100)
    ans2 = models.CharField(max_length=100)
    ans3 = models.CharField(max_length=100)
    ans4 = models.CharField(max_length=100)
    ans5 = models.CharField(max_length=100)
    correct_ans = models.CharField(max_length=100)

