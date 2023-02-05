from django.contrib import admin
from .models import CustomUser, UserLanguage, Experience

# Register your models here.

admin.site.register(CustomUser)
admin.site.register(UserLanguage)
admin.site.register(Experience)