from rest_framework import serializers
from .models import Product, Collection
from decimal import Decimal


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    price_with_tax = serializers.SerializerMethodField(method_name="calc_tax")
    # collection_id = serializers.PrimaryKeyRelatedField(
    #     queryset=Collection.objects.all(), source="collection"
    # )  # returns id of collection

    Collection_name = serializers.StringRelatedField(source="collection")

    def calc_tax(self, product: Product):
        return product.price * Decimal(1.1)
