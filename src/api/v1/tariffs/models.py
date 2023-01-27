from django.db import models


class Advantage(models.Model):
    advantage_type =
    value =
    price


class Tariff(models.Model):
    advantages = models.ManyToManyField(TariffAdvantage)
    price


class ProductTariff(models.Model):
    product_id
    tariff_id
    advantages = ManyToManyField
    date_created
