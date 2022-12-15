from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from monografias.models import Monography
from monografias.serializers import MonographySerializer
from rest_framework.permissions import AllowAny

class MonographyAPI(APIView):
  def get(self, request, id=None):
    if id is not None:
        monography = Monography.objects.get(pk=id)
        serializer = MonographySerializer(monography, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    monographys = Monography.objects.all().order_by('name')
    serializer = MonographySerializer(monographys, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
    
  
  def post(self, request):
    serializer = MonographySerializer(data=request.data)
    if not serializer.is_valid():
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    serializer.save()

    return Response(serializer.data, status=status.HTTP_200_OK)
  
  def put(self, request, id):
    monography = Monography.objects.get(pk=id)
    serializer = MonographySerializer(instance=monography, data=request.data)
    if not serializer.is_valid():
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    serializer.save()

    return Response(serializer.data, status=status.HTTP_200_OK)

  def delete(self, request, id):
    monography = Monography.objects.get(pk=id)
    monography.delete()
    return Response(status=status.HTTP_200_OK)