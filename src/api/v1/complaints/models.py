from django.db import models
from api.v1.accounts.models import CustomUser
from api.v1.products.models import Product


class Complaint(models.Model):
    creator = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=500)
    date_create = models.DateField(auto_now_add=True)


class ProductComplaint(models.Model):
    complaint = models.ForeignKey(Complaint, on_delete=models.CASCADE)
    client = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
    date_create = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.text