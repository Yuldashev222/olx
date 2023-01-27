from django.db import models


class Category(models.Model):
    name = chevrolet
    parent = models.ForeignKey('self', on_delete=models.CASCADE)


class Field(models.Model):
    name unique = True
    categories = models.ManyToManyField(Category)


class ProductField(models.Model):
    field_id
    text
    is_true
    product_id


class Product(models.Model):

