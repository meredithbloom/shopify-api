from rest_framework import serializers
from .models import Gadget, Location





# class LocationListingField(serializers.RelatedField):
#     def to_representation(self, value):
#         return value.name



class GadgetSerializer(serializers.ModelSerializer):
    #location_name = serializers.StringRelatedField(many=True)
    class Meta:
        model = Gadget
        fields = ('id', 'name', 'description', 'image_url', 'location')


class LocationSerializer(serializers.ModelSerializer):
    gadgets = GadgetSerializer(many=True, read_only=True)
    
    class Meta:
        model = Location
        fields = ('id', 'name', 'gadgets')
        
    def create(self, validated_data):
        inventory_data = validated_data.pop('gadgets')
        location = Location.objects.create(**validated_data)
        for gadget_data in inventory_data:
            Gadget.objects.create(location=location, **gadget_data)
        return location
    
    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.save()
        
    #     gadgets = validated_data.get('gadgets', instance.gadgets)
        
    #     for gadget in gadgets:
    #         gadget_id = gadget.get('id', None)
    #         if gadget_id:
    #             gadget_item = Gadget.objects.get(id=gadget_id, location=instance)
    #             gadget_item.name = gadget.get('name', gadget_item.name)
    #             gadget_item.description = gadget.get('description', gadget_item.description)
    #             gadget_item.image_url = gadget.get('image_url', gadget_item.image_url)
    #             gadget_item.save()
    #         else:
    #             Location.objects.create(name=instance, **gadget)
    #     return instance
                
            