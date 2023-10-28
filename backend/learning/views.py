from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ClosedEndedQuestion
from .serializers import ClosedEndedQuestionSerializer

class Test(APIView):

    def get(self, request):
        queryset = ClosedEndedQuestion.objects.all()
        serializer = ClosedEndedQuestionSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



