from django.shortcuts import render
from .models import Bus,Driver,DrowsinessEvent
from .serializers import DriverSerailizer,BusSerializer,DrowsinessEventSerializer
from rest_framework import generics

class DriverListCreateView(generics.ListCreateAPIView):
    queryset=Driver.objects.all()
    serializer_class=DriverSerailizer

class BusListCreateView(generics.ListCreateAPIView):
    queryset=Bus.objects.all()
    serializer_class=BusSerializer

class DrowsinessEventListCreateView(generics.ListCreateAPIView):
    queryset=DrowsinessEvent.objects.all()
    serializer_class=DrowsinessEventSerializer

