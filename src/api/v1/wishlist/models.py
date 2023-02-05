from django.db import models
from api.v1.accounts.models import CustomUser
from api.v1.products.models import Product


class WishlistProduct(models.Model):
    client = models.ForeignKey(CustomUser, related_name='wishlist_user', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='wishlists', on_delete=models.CASCADE)
    date_create = models.DateField(auto_now_add=True)


# class WishlistUser(models.Model):
#     client_user = models.ManyToManyField(CustomUser)
#     vendor_user = models.ManyToManyField(CustomUser)
#     date_create = models.DateField(auto_now_add=True)