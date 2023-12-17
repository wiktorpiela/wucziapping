from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from django.db.models import Q

from .models import ClosedEndedQuestion
from .serializers import ClosedEndedQuestionSerializer
  
class LearningGetClosedEndedQuestions(generics.ListAPIView):
    serializer_class = ClosedEndedQuestionSerializer

    def get_queryset(self):
        qCategory = self.request.data.get("questionCategory")
        queryset = ClosedEndedQuestion.objects.filter(Q(category_key__question_category__icontains=qCategory)).order_by("?")
        return queryset


        
    




