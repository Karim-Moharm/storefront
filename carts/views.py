from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Cart, CartItem
from .serializers import CartSerializer
from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import GenericViewSet


# you can't use model View set with carts
# because you don't need to get all carts or update a cart
class CartViewSet(CreateModelMixin, GenericViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
