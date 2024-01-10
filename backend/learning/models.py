from django.db import models

class ClosedEndedCategory(models.Model):
    question_category = models.CharField(max_length=25)

    def __str__(self) -> str:
        return self.question_category
    
class ClosedEndedCorrectAnswer(models.Model):
    question_correct_answer = models.CharField(max_length=150)

    def __str__(self):
        return self.question_correct_answer
    
class ClosedEndedIsMulti(models.Model):
    question_is_multi = models.SmallIntegerField()

    def __str__(self) -> str:
        return 'single' if self.question_is_multi==0 else 'multi'

class ClosedEndedPossibleAnswers(models.Model):
    question_possible_answers = models.CharField(max_length=300)

    def __str__(self) -> str:
        return self.question_possible_answers
    
class ClosedEndedTarget(models.Model):
    question_target = models.CharField(max_length=25)

    def __str__(self) -> str:
        return self.question_target

class ClosedEndedQuestion(models.Model):
    category = models.ForeignKey(ClosedEndedCategory, on_delete=models.CASCADE, related_name="question_cat")
    correct_answer = models.ForeignKey(ClosedEndedCorrectAnswer, on_delete=models.CASCADE, related_name="correct_ans")
    is_multi = models.ForeignKey(ClosedEndedIsMulti, on_delete=models.CASCADE, related_name="is_multi_quest")
    possible_answers = models.ForeignKey(ClosedEndedPossibleAnswers, on_delete=models.CASCADE, related_name="possible_ans")
    target = models.ForeignKey(ClosedEndedTarget, on_delete=models.CASCADE, related_name="question_txt")

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