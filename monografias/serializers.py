from rest_framework import serializers
from .models import Author, Advisor, Monography

class AuthorSerializer(serializers.ModelSerializer):
  class Meta:
    read_only_fields = ('id',)
    model = Author
    fields = '__all__'

class AdvisorSerializer(serializers.ModelSerializer):
  class Meta:
    read_only_fields = ('id',)
    model = Advisor
    fields = '__all__'
    

class MonographySerializer(serializers.ModelSerializer):
  class Meta:
    read_only_fields = ('id',)
    model = Monography
    fields = '__all__'