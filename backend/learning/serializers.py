from rest_framework import serializers
from .models import ClosedEndedQuestion, ClosedEndedQuestionCorrectAnswer, MyModel

class MySerializer(serializers.ModelSerializer):
    sliped_fields = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = MyModel
        fields = ['id', 'sliped_fields']

    def get_sliped_fields(self, obj):
        f_list =obj.my_field.split(',')
        return f_list

class ClosedEndedQuestionCorrectAnswerSerializer(serializers.ModelSerializer):
    correct_answer = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = ClosedEndedQuestionCorrectAnswer
        fields = '__all__'

    def get_correct_answer(self, obj):
        f_list =obj.correct_answer.split(',')
        return f_list


class ClosedEndedQuestionSerializer(serializers.ModelSerializer):
    category_key = serializers.StringRelatedField()
    question_text_key = serializers.StringRelatedField()
    possible_answers_key = serializers.StringRelatedField()
    correct_answer_key = ClosedEndedQuestionCorrectAnswerSerializer()
    is_multi_key = serializers.StringRelatedField()

    class Meta:
        model = ClosedEndedQuestion
        fields = '__all__' 