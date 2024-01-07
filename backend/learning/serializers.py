from rest_framework import serializers
from .models import (ClosedEndedQuestion, ClosedEndedQuestionCorrectAnswer, ClosedEndedQuestionPossibleAnswers, ClosedEndedQuestionCategory, OpenEndedQuestion, OpenEndedScope, OpenEndedWrongScope,)

class ClosedEndedQuestionCategorySerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model=ClosedEndedQuestionCategory
        fields=('id', 'category',)

    def get_category(self, obj):
        return obj.question_category.replace('Wybierz', '').strip()

class ClosedEndedQuestionCorrectAnswerSerializer(serializers.ModelSerializer):
    correct_answers = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = ClosedEndedQuestionCorrectAnswer
        fields = ('correct_answers',)

    def get_correct_answers(self, obj):
        f_list =obj.correct_answer.split(',')
        return f_list

class ClosedEndedQuestionPossibleAnswersSerializer(serializers.ModelSerializer):
    possible_answers = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model=ClosedEndedQuestionPossibleAnswers
        fields=('possible_answers',)

    def get_possible_answers(self, obj):
        if obj.I == "":
            return [obj.A, obj.B, obj.C, obj.D, obj.E, obj.F]
        else:
            return [obj.A, obj.B, obj.C, obj.D, obj.E, obj.F, obj.G, obj.H, obj.I]

class ClosedEndedQuestionSerializer(serializers.ModelSerializer):
    category_key = serializers.StringRelatedField()
    question_text_key = serializers.StringRelatedField()
    possible_answers_key = ClosedEndedQuestionPossibleAnswersSerializer()
    correct_answer_key = ClosedEndedQuestionCorrectAnswerSerializer()
    is_multi_key = serializers.StringRelatedField()

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