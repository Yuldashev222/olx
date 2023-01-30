from django.db import models
from accounts.models import CustomUser
from products.models import Product


class WishlistProduct(models.Model):
    client = models.ForeignKey(CustomUser, related_name='wishlistuser', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='wishlist_product', on_delete=models.CASCADE)
    create_date = models.DateField(auto_now_add=True)


class WishlistUser(models.Model):
    client_user = models.ManyToManyField(CustomUser)
    vendor_user = models.ManyToManyField(CustomUser)
    create_date = models.DateField(auto_now_add=True)
