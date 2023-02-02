from rest_framework import serializers
from .models import Product, Category, ProductField


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'image', 'parent')


class CategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'image', 'parent', 'creator', 'is_active')


class ProductFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductField
        exclude = ('product')


class ProductFieldCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductField
        fields = '__all__'


class ProductDetailSerializer(serializers.ModelSerializer):
    fields = ProductFieldSerializer()
    class Meta:
        model = Product
        exclude = ('auto_renewal', 'status', 'is_active', 'is_delete', 'date_update')


class ProductCreateSerializer(serializers.ModelSerializer):
    fields = ProductFieldSerializer()
    class Meta:
        model = Product
        exclude = ('views', 'status', 'is_active', 'is_delete', 'date_created', 'date_update')