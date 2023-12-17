from rest_framework import serializers
from .models import ClosedEndedQuestion

class ClosedEndedQuestionSerializer(serializers.ModelSerializer):
    category_key = serializers.StringRelatedField()
    question_text_key = serializers.StringRelatedField()
    possible_answers_key = serializers.StringRelatedField()
    correct_answer_key = serializers.StringRelatedField()
    is_multi_key = serializers.StringRelatedField()

    class Meta:
        model = ClosedEndedQuestion
        fields = '__all__' 