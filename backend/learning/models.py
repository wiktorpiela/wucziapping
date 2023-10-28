from django.db import models

class ClosedEndedQuestionPossibleAnswers(models.Model):
    A = models.CharField(max_length=25)
    B = models.CharField(max_length=25)
    C = models.CharField(max_length=25)
    D = models.CharField(max_length=25)
    E = models.CharField(max_length=25, null=True)

    def __str__(self) -> str:
        if self.E != "":
            return f"{self.A} - {self.B} - {self.C} - {self.D} - {self.E}"
        else:
            return f"{self.A} - {self.B} - {self.C} - {self.D}"

class ClosedEndedQuestionCorrectAnswer(models.Model):
    correct_answer = models.CharField(max_length=25)

    def __str__(self) -> str:
        return self.correct_answer

class ClosedEndedQuestionText(models.Model):
    question_text = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.question_text

class ClosedEndedQuestion(models.Model):
    question_text_id = models.ForeignKey(ClosedEndedQuestionText, on_delete=models.CASCADE, related_name="question_txt")
    possible_answers_id = models.ForeignKey(ClosedEndedQuestionPossibleAnswers, on_delete=models.CASCADE, related_name="possible_ans")
    correct_answer_id = models.ForeignKey(ClosedEndedQuestionCorrectAnswer, on_delete=models.CASCADE, related_name="correct_ans")
    is_hard = models.BooleanField(default=False)