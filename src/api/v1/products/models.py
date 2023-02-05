from django.db import models
from random import sample
from django.core.validators import MinValueValidator

from api.v1.accounts.models import CustomUser
from api.v1.accounts.services import upload_product_path
from api.v1.accounts.validators import validate_phone
from .enums import ValueType, Status


class Category(models.Model):
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=200, unique=True)
    date_created = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=False)

    creator = models.ForeignKey(CustomUser, related_name='categories', on_delete=models.PROTECT)

    def save(self, *args, **kwargs):
        self.name = ' '.join(self.name.strip().split())
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Field(models.Model):
    categories = models.ManyToManyField(Category)
    name = models.CharField(max_length=150, unique=True)
    date_created = models.DateField(auto_now_add=True)

    # creator = models.ForeignKey(CustomUser, related_name='categoriesField', on_delete=models.PROTECT)

    def save(self, *args, **kwargs):
        self.name = ' '.join(self.name.strip().split())
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Product(models.Model):
    number_id = models.CharField(max_length=8, unique=True)
    author = models.ForeignKey(CustomUser, related_name='products', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    title = models.CharField(max_length=250)
    description = models.TextField(max_length=9000, blank=True)
    value_type = models.CharField(max_length=1, choices=ValueType.choices())
    price = models.FloatField(default=0, validators=[MinValueValidator(0.0)])
    price_is_dollar = models.BooleanField(default=False)
    agreement = models.BooleanField(default=False)
    new = models.BooleanField(default=False)
    business = models.BooleanField(default=False)
    region = models.CharField(max_length=50)
    district = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=13, validators=[validate_phone])
    auto_renewal = models.BooleanField(default=False)
    views = models.PositiveSmallIntegerField(default=0)
    status = models.CharField(max_length=2, choices=Status.choices())
    date_created = models.DateField(auto_now_add=True)
    date_update = models.DateField(auto_now_add=True)

    # Image
    main_image = models.ImageField(upload_to=upload_product_path, blank=True)
    image1 = models.ImageField(upload_to=upload_product_path, blank=True)
    image2 = models.ImageField(upload_to=upload_product_path, blank=True)
    image3 = models.ImageField(upload_to=upload_product_path, blank=True)
    image4 = models.ImageField(upload_to=upload_product_path, blank=True)
    image5 = models.ImageField(upload_to=upload_product_path, blank=True)

    is_active = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.number_id = sample(range(100), 8)
        if Product.objects.filter(number_id=self.number_id).exists():
            self.number_id = sample(range(10), 8)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class ProductField(models.Model):
    field = models.ForeignKey(Field, on_delete=models.CASCADE)
    text = models.CharField(max_length=255, blank=True)
    is_true = models.BooleanField(default=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.product} {self.field}'