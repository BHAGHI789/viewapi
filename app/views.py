from django.shortcuts import render
from app.models import Student
from app.serializer import Studentserializer
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView,ListCreateAPIView,RetrieveDestroyAPIView,RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView

# Create your views here.
class Studentlist(ListAPIView):
    queryset=Student.objects.all()
    serializer_class=Studentserializer
class create_student(CreateAPIView):
    queryset=Student.objects.all()
    serializer_class=Studentserializer
class retive_student(RetrieveAPIView):
    queryset=Student.objects.all()
    serializer_class=Studentserializer
class update_student(UpdateAPIView):
    queryset=Student.objects.all()
    serializer_class=Studentserializer
class destroy_student(DestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=Studentserializer
class student_listcreate(ListCreateAPIView):
    queryset=Student.objects.all()
    serializer_class=Studentserializer
    
class student_rede(RetrieveDestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=Studentserializer


class student_reup(RetrieveUpdateAPIView):
    queryset=Student.objects.all()
    serializer_class=Studentserializer
class student_reupde(RetrieveUpdateDestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=Studentserializer
