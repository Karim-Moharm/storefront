from django.db import models
from store.models import Product
from uuid import uuid4

# Create your models here.


class Cart(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    created_at = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="cartitem")
    quantity = models.PositiveSmallIntegerField()
    # both cart and product can have many cart item
    # you can add as many items in the cat of one product
    # diffrence between cartItem and product
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="productitem"
    )

    class Meta:
        unique_together = [["cart", "product"]]
