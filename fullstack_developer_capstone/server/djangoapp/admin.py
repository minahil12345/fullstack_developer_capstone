from django.contrib import admin
from .models import CarMake
from .models import CarModel

admin.site.register(CarMake)
admin.site.register(CarModel)