from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class Test(APIView):

    def get(self, request):
        return Response({"output": "testview"}, status=status.HTTP_200_OK)



