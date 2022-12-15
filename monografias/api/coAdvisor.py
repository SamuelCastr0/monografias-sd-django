from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from monografias.models import CoAdvisor
from monografias.serializers import CoAdvisorSerializer

class CoAdvisorAPI(APIView):
  def get(self, request, id=None):
    if id:
        coAdvisor = CoAdvisor.objects.get(pk=id)
        serializer = CoAdvisorSerializer(coAdvisor, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    coAdvisors = CoAdvisor.objects.all().order_by('name')
    serializer = CoAdvisorSerializer(coAdvisors, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
    
  
  def post(self, request):
    serializer = CoAdvisorSerializer(data=request.data)
    if not serializer.is_valid():
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    serializer.save()

    return Response(serializer.data, status=status.HTTP_200_OK)
  
  def put(self, request, id):
    coAdvisor = CoAdvisor.objects.get(pk=id)
    serializer = CoAdvisorSerializer(instance=coAdvisor, data=request.data)
    if not serializer.is_valid():
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    serializer.save()

    return Response(serializer.data, status=status.HTTP_200_OK)

  def delete(self, request, id):
    coAdvisor = CoAdvisor.objects.get(pk=id)
    coAdvisor.delete()
    return Response(status=status.HTTP_200_OK)