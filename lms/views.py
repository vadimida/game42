from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet
from lms.models import Student, Curator
from lms.serializers import StudentSerializer,CuratorSerializer
class StudentViewSet(
    viewsets.ModelViewSet
):
    queryset=Student.objects.all()
    serialzer_class=StudentSerializer
    permission_classes=[IsAuthenticatedOrReadOnly,]

class CuratorViewSet(
    viewsets.ModelViewSet
):
    queryset = Curator.objects.all()
    serialzer_class = CuratorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, ]

# Create your views here.
