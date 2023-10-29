from rest_framework import serializers
from .models import ClosedEndedQuestion

class ClosedEndedQuestionSerializer(serializers.ModelSerializer):
    question_text = serializers.StringRelatedField()
    possible_answers = serializers.StringRelatedField()
    correct_answer = serializers.StringRelatedField()

    class Meta:
        model = ClosedEndedQuestion
        fields = ("id","question_text", "possible_answers", "correct_answer", "is_hard",)