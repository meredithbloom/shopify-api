from django.shortcuts import render
from .serializers import GadgetSerializer, LocationSerializer
from rest_framework import generics
from .models import Gadget, Location

# Create your views here.

class GadgetList(generics.ListCreateAPIView):
    queryset = Gadget.objects.all().order_by('id')
    serializer_class = GadgetSerializer
    

class GadgetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Gadget.objects.all().order_by('id')
    serializer_class = GadgetSerializer
    



class LocationList(generics.ListCreateAPIView):
    queryset = Location.objects.all().order_by('id')
    serializer_class = LocationSerializer
    
    
class LocationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Location.objects.all().order_by('id')
    serializer_class = LocationSerializer
    
    
