from rest_framework import serializers
from .models import Cart, CartItem
from store.serializers import ProductSerializer
from store.models import Product
from decimal import Decimal


class SimpleProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "title", "price"]


class CartItemSerializer(serializers.ModelSerializer):
    product = SimpleProductSerializer()
    total_price = serializers.SerializerMethodField()

    def get_total_price(self, cartitem):
        return cartitem.product.price * cartitem.quantity

    class Meta:
        model = CartItem
        fields = ["id", "quantity", "product", "total_price"]


class CartSerializer(serializers.ModelSerializer):
    cartitem = CartItemSerializer(many=True, read_only=True)
    id = serializers.UUIDField(read_only=True)
    total_price = serializers.SerializerMethodField()

    def get_total_price(self, cart):
        total = 0
        for item in cart.cartitem.all():
            total += item.product.price * item.quantity
        return total

    class Meta:
        model = Cart
        fields = ["id", "cartitem", "total_price"]
