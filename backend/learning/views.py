from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from django.db.models import Q

from .models import ClosedEndedQuestion, ClosedEndedQuestionCorrectAnswer, ClosedEndedQuestionPossibleAnswers
from .serializers import ClosedEndedQuestionSerializer, ClosedEndedQuestionCorrectAnswerSerializer, ClosedEndedQuestionPossibleAnswersSerializer
  
class LearningGetClosedEndedQuestions(generics.ListAPIView):
    serializer_class = ClosedEndedQuestionSerializer

    def get_queryset(self):
        qCategory = self.request.data.get("questionCategory")
        queryset = ClosedEndedQuestion.objects.filter(Q(category_key__question_category__icontains=qCategory)).order_by("?")
        return queryset
    
class Test(generics.ListAPIView):
    serializer_class = ClosedEndedQuestionPossibleAnswersSerializer
    queryset = ClosedEndedQuestionPossibleAnswers.objects.all()



        
    




