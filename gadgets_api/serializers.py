from rest_framework import serializers
from .models import Gadget, Location


class GadgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gadget
        fields = ('id', 'name', 'description', 'image_url', 'location')


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'name')