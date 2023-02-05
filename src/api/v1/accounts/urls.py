from django.urls import path
from .views import StaffRegisterAPIView, ClientRegisterAPIView, UserRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('register/staff/', StaffRegisterAPIView.as_view()),
    path('register/client/', ClientRegisterAPIView.as_view()),
    path('user/<int:pk>/', UserRetrieveUpdateDestroyAPIView.as_view())
]
