from rest_framework import serializers
from .models import Gadget, Location


class GadgetSerializer(serializers.ModelSerializer):
    location_name = serializers.StringRelatedField()
    class Meta:
        model = Gadget
        fields = ('id', 'name', 'description', 'image_url', 'location', 'location_name')


class LocationSerializer(serializers.ModelSerializer):
    gadgets = GadgetSerializer(many=True)
    
    class Meta:
        model = Location
        fields = ('id', 'name', 'gadgets')