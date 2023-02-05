from django.urls import path
from .views import CategoriesAPIViews

urlpatterns = [
    path('categories/', CategoriesAPIViews.as_view())
]
