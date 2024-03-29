from rest_framework import generics
from django.db.models import Q
from .models import OpenEndedQuestion, ClosedEndedQuestion
from .serializers import OpenEndedQuestionSerializer, ClosedEndedQuestionSerializer
  
class GetClosedEndedQuestions(generics.ListAPIView):
    serializer_class = ClosedEndedQuestionSerializer

    def get_queryset(self):
        qCategory = self.request.data.get("questionCategory")
        queryset = ClosedEndedQuestion.objects.all() #filter(Q(category__question_category__icontains=qCategory)).order_by("?")
        return queryset
    
# class ClosedEndedQuestionsCategories(generics.ListAPIView):
#     serializer_class = ClosedEndedQuestionCategorySerializer
#     queryset = ClosedEndedQuestionCategory.objects.all()

    
class Test(generics.ListAPIView):
    serializer_class = OpenEndedQuestionSerializer
    queryset = OpenEndedQuestion.objects.all()



        
    




