from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from monografias.models import Author
from monografias.serializers import AuthorSerializer

class AuthorAPI(APIView):
  def get(self, request, id=None):
    if id is not None:
        author = Author.objects.get(pk=id)
        serializer = AuthorSerializer(author, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    authors = Author.objects.all().order_by('name')
    serializer = AuthorSerializer(authors, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
    
  
  def post(self, request):
    serializer = AuthorSerializer(data=request.data)
    if not serializer.is_valid():
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    serializer.save()

    return Response(serializer.data, status=status.HTTP_200_OK)
  
  def put(self, request, id):
    author = Author.objects.get(pk=id)
    serializer = AuthorSerializer(instance=author, data=request.data)
    if not serializer.is_valid():
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    serializer.save()

    return Response(serializer.data, status=status.HTTP_200_OK)

  def delete(self, request, id):
    author = Author.objects.get(pk=id)
    author.delete()
    return Response(status=status.HTTP_200_OK)