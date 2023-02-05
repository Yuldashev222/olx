from django.contrib import admin
from .models import Category, Field, Product, ProductField

# Register your models here.

admin.site.register(Category)
admin.site.register(Field)
admin.site.register(Product)
admin.site.register(ProductField)