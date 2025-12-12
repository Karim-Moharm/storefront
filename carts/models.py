from django.db import models
from store.models import Product

# Create your models here.


class Cart(models.Model):
    # auto_nor or auto_now_add
    created_at = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
    quatity = models.PositiveSmallIntegerField()
    # both cart and product can have many cart item
    # you can add as many items in the cat of one product
    # diffrence between cartItem and product
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
