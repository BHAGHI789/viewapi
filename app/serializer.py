from rest_framework import serializers
from app.models import Student
class Studentserializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'