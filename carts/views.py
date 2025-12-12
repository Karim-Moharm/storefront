from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Cart, CartItem
from .serializers import CartSerializer, CartItemSerializer
from rest_framework.mixins import (
    CreateModelMixin,
    RetrieveModelMixin,
    DestroyModelMixin,
    ListModelMixin,
)
from rest_framework.viewsets import GenericViewSet


# you can't use model View set with carts
# because you don't need to get all carts or update a cart
class cartViewSet(
    CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, GenericViewSet
):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CartItemViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
