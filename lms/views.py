from django.shortcuts import render
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from lms.models import Student
from lms.serializers import StudentSerializer
class StudentViewSet(ModelViewSet):
    queryset=Student.objects.all()
    serialzer_class=StudentSerializer
    permission_classes=[IsAuthenticatedOrReadOnly,]

# Create your views here.
