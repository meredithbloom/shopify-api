from rest_framework import serializers
from .models import Gadget, Location





class LocationListingField(serializers.RelatedField):
    def to_representation(self, value):
        return value.name



class GadgetSerializer(serializers.ModelSerializer):
    #location_name = serializers.StringRelatedField(many=True)
    class Meta:
        model = Gadget
        fields = ('id', 'name', 'description', 'image_url', 'location')


class LocationSerializer(serializers.ModelSerializer):
    gadgets = GadgetSerializer(many=True)
    
    class Meta:
        model = Location
        fields = ('id', 'name', 'gadgets')
        
    def create(self, validated_data):
        inventory_data = validated_data.pop('gadgets')
        location = Location.objects.create(**validated_data)
        for gadget_data in inventory_data:
            Gadget.objects.create(location=location, **gadget_data)
        return location