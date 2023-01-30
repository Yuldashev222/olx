from django.db import models
from uuid import uuid4
from random import sample

from api.v1.accounts.models import CustomUser
from api.v1.accounts.validators import validate_phone


class Category(models.Model):
    parent = models.ForeignKey('self', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, unique=True)
    date_created = models.DateField(auto_now_add=True)

    # creator !

    def save(self, *args, **kwargs):
        self.name = ' '.join(self.name.strip().split())
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Field(models.Model):
    categories = models.ManyToManyField(Category)
    name = models.CharField(max_length=150, unique=True)
    date_created = models.DateField(auto_now_add=True)

    # creator !

    def __str__(self):
        return self.name


class Product(models.Model):
    # status = 4 ta jarayon
    __id = models.CharField(max_length=8, unique=True)
    author = models.ForeignKey(CustomUser, related_name='products', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    price = models.FloatField(default=0)  # minimum 0
    price_is_dollar = models.BooleanField(default=False)
    # kelishiladimi yoqmi
    # obmen gami ? booleanfield
    # eskimi yangimi booleanfield
    # views
    title = models.CharField(max_length=250)
    description = models.TextField(max_length=9000, blank=True)
    region = models.CharField(max_length=50)
    district = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=13, validators=[validate_phone])
    # 30 kun qoshish

    # Image
    main_image = models.ImageField(upload_to='')
    image1 = models.ImageField(upload_to='')
    image2 = models.ImageField(upload_to='')
    image3 = models.ImageField(upload_to='')
    image4 = models.ImageField(upload_to='')
    image5 = models.ImageField(upload_to='')

    is_deleted = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.__id = sample(range(100), 8)
        if Product.objects.filter(__id=self.__id).exists():
            self.__id = sample(range(100), 8)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class ProductField(models.Model):
    field = models.ForeignKey(Field, on_delete=models.CASCADE)
    text = models.CharField(max_length=255, blank=True)
    is_true = models.BooleanField(default=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
