from django.db import models
from accounts.servises import upload_tariff_path
from products.models import Product


class Advantage(models.Model):
    TYPE_CHOICE = (
        ('top', 'TOP'),
        ('kotarish', 'KO\'TARISH'),
        ('vip', 'VIP'),
    )
    type = models.CharField(max_length=8, choices=TYPE_CHOICE, default=TYPE_CHOICE[0][0])
    value = models.PositiveSmallIntegerField()
    price = models.FloatField()
    create_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.value} {self.type}'
    


class Tariff(models.Model):
    advantages = models.ManyToManyField(Advantage)
    name = models.CharField(max_length=50, unique=True)
    logo = models.ImageField(upload_to=upload_tariff_path)
    price = models.FloatField()
    create_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
    



class ProductTariff(models.Model):
    product_id = models.ForeignKey(Product, related_name='product_tariff', on_delete=models.CASCADE)
    tariff_id = models.ManyToManyField(Tariff)
    advantages = models.ManyToManyField(Advantage)
    create_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.product_id
