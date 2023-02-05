from django.db import models
from api.v1.accounts.services import upload_tariff_path
from api.v1.accounts.models import CustomUser
from api.v1.products.models import Product


class Advantage(models.Model):
    TYPE_CHOICE = (
        ('t', 'TOP'),
        ('k', 'KO\'TARISH'),
        ('v', 'VIP'),
    )

    creator = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    type = models.CharField(max_length=1, choices=TYPE_CHOICE)
    value = models.PositiveSmallIntegerField()
    price = models.FloatField()
    date_create = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.value} {self.type}'


class Tariff(models.Model):
    creator = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    advantages = models.ManyToManyField(Advantage)
    name = models.CharField(max_length=50, unique=True)
    logo = models.ImageField(upload_to=upload_tariff_path)
    price = models.FloatField()
    date_create = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.name = ' '.join(self.name.strip().split())
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class ProductTariff(models.Model):
    product = models.ForeignKey(Product, related_name='tariffs', on_delete=models.CASCADE)
    tariff = models.ForeignKey(Tariff, on_delete=models.PROTECT, blank=True)
    advantages = models.ManyToManyField(Advantage, blank=True)
    date_create = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.product_id