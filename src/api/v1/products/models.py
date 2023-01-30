from django.db import models
from accounts.models import CustomUser
from accounts.validators import validate_phone


class Category(models.Model):
    parent = models.ForeignKey('self', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    create_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
    


class Field(models.Model):
    categories = models.ManyToManyField(Category)
    name = models.CharField(max_length=150, unique=True)
    create_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.name


class CategoryField(models.Model):
    field_id = models.ForeignKey(Field, on_delete=models.CASCADE)
    text = models.CharField(max_length=150)
    is_true = models.BooleanField(default=False)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.text
    

class Product(models.Model):
    author = models.ForeignKey(CustomUser, related_name='product_user', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    title = models.CharField(max_length=250)
    description = models.TextField()
    location = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=13, unique=True, validators=[validate_phone])

    # Image
    image = models.ImageField(upload_to=None)
    image1 = models.ImageField(upload_to=None)
    image2 = models.ImageField(upload_to=None)
    image3 = models.ImageField(upload_to=None)
    image4 = models.ImageField(upload_to=None)
    image5 = models.ImageField(upload_to=None)

    def __str__(self):
        return self.title
    