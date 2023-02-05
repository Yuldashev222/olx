from django.contrib import admin
from .models import Advantage, Tariff, ProductTariff

# Register your models here.

admin.site.register(Advantage)
admin.site.register(Tariff)
admin.site.register(ProductTariff)