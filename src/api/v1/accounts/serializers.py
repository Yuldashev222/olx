from rest_framework import serializers

from .models import CustomUser


class StaffRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['phone_number', 'email', 'password']

    def create(self, validated_data):
        instance = CustomUser.objects.create_user(is_staff=True, **validated_data)
        return instance
    
class ClientRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['phone_number', 'email', 'password']

    def create(self, validated_data):
        instance = CustomUser.objects.create_user(**validated_data)
        return instance

class UserSerializer(serializers.ModelSerializer):
    date_joined = serializers.DateTimeField(format='%Y-%m-%d %H:%M', read_only=True)
    class Meta:
        model = CustomUser
        exclude = ['is_active', 'is_deleted', 'is_staff', 'password']