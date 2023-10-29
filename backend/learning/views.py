from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from .models import ClosedEndedQuestion, ClosedEndedQuestionText
from .serializers import ClosedEndedQuestionSerializer
from django.db.models import Q
import json
  
class LearningGetClosedEndedQuestions(generics.ListAPIView):
    serializer_class = ClosedEndedQuestionSerializer

    def get_queryset(self):
        isHard = self.request.data.get("isHard")
        questionType = self.request.data.get("questionType")
        queryset = ClosedEndedQuestion.objects.filter(Q(is_hard=isHard) & Q(question_text__question_text__icontains=questionType)).order_by("?")
        return queryset
    
class QuestionTypesDifficultyLevel(APIView):

    def get(self, request):
        questTypes = ClosedEndedQuestionText.objects.all().values_list("question_text", flat=True)
        isEasyList = []
        for qtype in questTypes:
            isEasy = ClosedEndedQuestion.objects.filter(Q(question_text__question_text__icontains=qtype) & Q(is_hard=0)).exists()
            isEasyList.append(isEasy)

        serialized = json.dumps(zip(questTypes, isEasyList))
            
        return Response({"types":serialized}, status=status.HTTP_200_OK)


        
    




