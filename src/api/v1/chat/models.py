from django.db import models
from accounts.models import CustomUser
from products.models import Product


class Message(models.Model):
    client = models.ForeignKey(CustomUser, related_name='messages', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    text = models.CharField(max_length=250)
    date_create = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.text
