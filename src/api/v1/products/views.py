from rest_framework import (
    generics
)

from .models import Category
from .serializers import CategoriesSerializer
# Create your views here.

class CategoriesAPIViews(generics. ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoriesSerializer