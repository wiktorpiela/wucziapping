from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from .models import ClosedEndedQuestion, ClosedEndedQuestionCategory
from .serializers import ClosedEndedQuestionSerializer
from django.db.models import Q
  
class LearningGetClosedEndedQuestions(generics.ListAPIView):
    serializer_class = ClosedEndedQuestionSerializer

    def get_queryset(self):
        isHard = self.request.data.get("isHard")
        qCategory = self.request.data.get("questionCategory")
        queryset = ClosedEndedQuestion.objects.filter(Q(is_hard=isHard) & Q(question_category__question_category__icontains=qCategory)).order_by("?")
        return queryset
    
class QuestionCategoryDifficultyLevel(APIView):

    def get(self, request):
        categories = ClosedEndedQuestionCategory.objects.all().values_list("question_category", flat=True)
        isEasyList = []
        for qcat in categories:
            isEasy = ClosedEndedQuestion.objects.filter(Q(question_category__question_category__icontains=qcat) & Q(is_hard=0)).exists()
            isEasyList.append(isEasy)

        question_types = {"questionTypes":list(categories),
                          "isEasy":isEasyList}
        
        return Response({"types":question_types}, status=status.HTTP_200_OK)


        
    




