from django.db import models

class ClosedEndedQuestionPossibleAnswers(models.Model):
    A = models.CharField(max_length=20)
    B = models.CharField(max_length=20)
    C = models.CharField(max_length=20)
    D = models.CharField(max_length=20)
    E = models.CharField(max_length=20)
    F = models.CharField(max_length=20)
    G = models.CharField(max_length=20, null=True)
    H = models.CharField(max_length=20, null=True)
    I = models.CharField(max_length=20, null=True)

    def __str__(self) -> str:
        if self.I != "":
            return f"{self.A} - {self.B} - {self.C} - {self.D} - {self.E} - {self.F} - {self.G}, - {self.H} - {self.I}"
        else:
            return f"{self.A} - {self.B} - {self.C} - {self.D} - {self.E} - {self.F}"

# class ClosedEndedQuestionCorrectAnswer(models.Model):
#     correct_answer = models.CharField(max_length=25)

#     def __str__(self) -> str:
#         return self.correct_answer

# class ClosedEndedQuestionText(models.Model):
#     question_text = models.CharField(max_length=200)

#     def __str__(self) -> str:
#         return self.question_text
    
# class ClosedEndedQuestionCategory(models.Model):
#     question_category = models.CharField(max_length=200)

# class ClosedEndedQuestion(models.Model):
#     question_category = models.ForeignKey(ClosedEndedQuestionCategory, on_delete=models.CASCADE, related_name="question_cat")
#     question_text = models.ForeignKey(ClosedEndedQuestionText, on_delete=models.CASCADE, related_name="question_txt")
#     possible_answers = models.ForeignKey(ClosedEndedQuestionPossibleAnswers, on_delete=models.CASCADE, related_name="possible_ans")
#     correct_answer = models.ForeignKey(ClosedEndedQuestionCorrectAnswer, on_delete=models.CASCADE, related_name="correct_ans")
#     is_hard = models.SmallIntegerField()

    