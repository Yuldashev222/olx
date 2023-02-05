from django.contrib import admin
from .models import Complaint, ProductComplaint

# Register your models here.

admin.site.register(Complaint)
admin.site.register(ProductComplaint)