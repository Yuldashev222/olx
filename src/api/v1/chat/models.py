from django.db import models
from accounts.models import CustomUser
from products.models import Product


class Message(models.Model):
    user = models.ForeignKey(CustomUser, related_name='messageuser', on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)
    text = models.CharField(max_length=250)
    create_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.text