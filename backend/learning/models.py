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
            return f"{self.A},{self.B},{self.C},{self.D},{self.E},{self.F},{self.G},{self.H},{self.I}"
        else:
            return f"{self.A},{self.B},{self.C},{self.D},{self.E},{self.F}"

class ClosedEndedQuestionText(models.Model):
    question_text = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.question_text
    
class ClosedEndedQuestionCategory(models.Model):
    question_category = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.question_category

class ClosedEndedQuestionCorrectAnswer(models.Model):
    correct_answer = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.correct_answer
    
class ClosedEndedQuestionIsMulti(models.Model):
    isMulti = models.SmallIntegerField()

    def __str__(self) -> str:
        if self.isMulti==0:
            return 'single'
        else:
            return 'multi'

class ClosedEndedQuestion(models.Model):
    category_key = models.ForeignKey(ClosedEndedQuestionCategory, on_delete=models.CASCADE, related_name="question_cat")
    possible_answers_key = models.ForeignKey(ClosedEndedQuestionPossibleAnswers, on_delete=models.CASCADE, related_name="possible_ans")
    question_text_key = models.ForeignKey(ClosedEndedQuestionText, on_delete=models.CASCADE, related_name="question_txt")
    correct_answer_key = models.ForeignKey(ClosedEndedQuestionCorrectAnswer, on_delete=models.CASCADE, related_name="correct_ans")
    is_multi_key = models.ForeignKey(ClosedEndedQuestionIsMulti, on_delete=models.CASCADE, related_name="is_multi_quest")

# open ended question models ----------------------

class OpenEndedCategory(models.Model):
    question_category = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.question_category
    
class OpenEndedTarget(models.Model):
    question_target = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.question_target
    
class OpenEndedScope(models.Model):
    question_scope = models.CharField(max_length=300)

    def __str__(self) -> str:
        return self.question_scope

class OpenEndedWrongScope(models.Model):
    question_wrong_scope = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self) -> str:
        return self.question_wrong_scope
    
class OpenEndedQuestion(models.Model):
    category = models.ForeignKey(OpenEndedCategory, on_delete=models.CASCADE, related_name='question_cat_open')
    target = models.ForeignKey(OpenEndedTarget, on_delete=models.CASCADE, related_name='question_target_open')
    scope = models.ForeignKey(OpenEndedScope, on_delete=models.CASCADE, related_name='question_scope_open')
    wrong_scope = models.ForeignKey(OpenEndedWrongScope, on_delete=models.CASCADE, related_name='question_wrong_scope_open')   