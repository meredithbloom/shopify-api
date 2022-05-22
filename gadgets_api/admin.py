from django.contrib import admin
from .models import Gadget
from .models import Location

# Register your models here.
admin.site.register(Gadget)
admin.site.register(Location)
