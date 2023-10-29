from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from .models import ClosedEndedQuestion
from .serializers import ClosedEndedQuestionSerializer
from django.db.models import Q
  
class LearningGetClosedEndedQuestions(generics.ListAPIView):
    serializer_class = ClosedEndedQuestionSerializer

    def get_queryset(self):
        isHard = self.request.data.get("isHard")
        questionType = self.request.data.get("questionType")
        queryset = ClosedEndedQuestion.objects.filter(Q(is_hard=isHard) & Q(question_text__question_text__icontains=questionType))
        return queryset
        
    




