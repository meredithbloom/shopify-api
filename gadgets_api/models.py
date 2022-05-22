from django.db import models

# Create your models here.
class Gadget(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=400, blank=True)
    image_url = models.CharField(max_length=255, blank=True)
    location = models.ForeignKey("Location",related_name="gadgets", on_delete=models.CASCADE, blank=True)
    
    def __str__(self):
        return '%d: %s' % (self.id, self.name)
    
    # def new_gadget(self, name):
    #     gadget = self.create(name=name)
    #     return gadget


#potentially adding inventory caps for various locations - some locations have more available storage than others
#potentially counting various types of objects
class Location(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name