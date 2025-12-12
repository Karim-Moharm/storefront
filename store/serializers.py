from rest_framework import serializers
from .models import Product, Collection, Order
from decimal import Decimal


class CollectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Collection
        fields = ["id", "title"]


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "id",
            "title",
            "price",
            "price_with_tax",
            "collection",
            "description",
            "slug",
            "inventory",
        ]

    price_with_tax = serializers.SerializerMethodField(method_name="calc_tax")

    # collection = serializers.HyperlinkedRelatedField(
    #     query_set=Collection.objects.all(), view_name="collection_details"
    # )

    def calc_tax(self, product: Product):
        return product.price * Decimal(1.1)


class OderSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["id", "placed_at", "payment_status"]
