from rest_framework import serializers
from .models import ClosedEndedCorrectAnswer, ClosedEndedPossibleAnswers, ClosedEndedQuestion, OpenEndedQuestion, OpenEndedScope, OpenEndedWrongScope,)

class ClosedEndedCorrectAnswerSerializer(serializers.ModelSerializer):
    correct_answers = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = ClosedEndedCorrectAnswer
        fields = ('correct_answers',)

    def get_question_correct_answers(self, obj):
        f_list =obj.correct_answer.split(',')
        return f_list

class ClosedEndedPossibleAnswersSerializer(serializers.ModelSerializer):
    possible_answers = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model=ClosedEndedPossibleAnswers
        fields=('possible_answers',)

    def get_question_possible_answers(self, obj):
        f_list =obj.possible_answers.split(',')
        return f_list

class ClosedEndedQuestionSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    target = serializers.StringRelatedField()
    possible_answers = ClosedEndedPossibleAnswersSerializer()
    correct_answer = ClosedEndedCorrectAnswerSerializer()
    is_multi = serializers.StringRelatedField()

    class Meta:
        model = ClosedEndedQuestion
        fields = '__all__' 

# open ended questions serializers      
class OpenEndedScopeSerializer(serializers.ModelSerializer):
    question_scope = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model=OpenEndedScope
        fields = ('question_scope',)

    def get_question_scope(self, obj):
        f_list = obj.question_scope.split(',')
        return f_list
    
class OpenEndedWrongScopeSerializer(serializers.ModelSerializer):
    question_wrong_scope = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = OpenEndedWrongScope
        fields = ('question_wrong_scope',)

    def get_question_wrong_scope(self, obj):
        field_val =  obj.question_wrong_scope
        if field_val == '':
            return []
        else:
            f_list = field_val.split(',')
        return f_list


class OpenEndedQuestionSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    target = serializers.StringRelatedField()
    scope = OpenEndedScopeSerializer()
    wrong_scope = OpenEndedWrongScopeSerializer()

    class Meta:
        model = OpenEndedQuestion
        fields = '__all__'