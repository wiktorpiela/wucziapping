from django.db import models

class ClosedEndedQuestionPossibleAnswers(models.Model):
    A = models.CharField(max_length=25)
    B = models.CharField(max_length=25)
    C = models.CharField(max_length=25)
    D = models.CharField(max_length=25)
    E = models.CharField(max_length=25, null=True)

    def __str__(self) -> str:
        if self.E != "":
            return f"A.{self.A} - B.{self.B} - C.{self.C} - D.{self.D} - E.{self.E}"
        else:
            return f"A.{self.A} - B.{self.B} - C.{self.C} - D.{self.D}"

class ClosedEndedQuestionCorrectAnswer(models.Model):
    correct_answer = models.CharField(max_length=25)

    def __str__(self) -> str:
        return self.correct_answer

class ClosedEndedQuestionText(models.Model):
    question_text = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.question_text

class ClosedEndedQuestion(models.Model):
    question_text = models.ForeignKey(ClosedEndedQuestionText, on_delete=models.CASCADE, related_name="question_txt")
    possible_answers = models.ForeignKey(ClosedEndedQuestionPossibleAnswers, on_delete=models.CASCADE, related_name="possible_ans")
    correct_answer = models.ForeignKey(ClosedEndedQuestionCorrectAnswer, on_delete=models.CASCADE, related_name="correct_ans")
    is_hard = models.BooleanField(default=False)