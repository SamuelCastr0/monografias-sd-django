from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from monografias.models import Advisor
from monografias.serializers import AdvisorSerializer

class AdvisorAPI(APIView):
  def get(self, request, id=None):
    if id is not None:
        advisor = Advisor.objects.get(pk=id)
        serializer = AdvisorSerializer(advisor, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    advisors = Advisor.objects.all().order_by('name')
    serializer = AdvisorSerializer(advisors, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
    
  
  def post(self, request):
    serializer = AdvisorSerializer(data=request.data)
    if not serializer.is_valid():
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    serializer.save()

    return Response(serializer.data, status=status.HTTP_200_OK)
  
  def put(self, request, id):
    advisor = Advisor.objects.get(pk=id)
    serializer = AdvisorSerializer(instance=advisor, data=request.data)
    if not serializer.is_valid():
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    serializer.save()

    return Response(serializer.data, status=status.HTTP_200_OK)

  def delete(self, request, id):
    advisor = Advisor.objects.get(pk=id)
    advisor.delete()
    return Response(status=status.HTTP_200_OK)