from rest_framework import serializers
from .models import Product, Collection, Order, Review, Customer
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


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ["name", "description", "created_at"]

        # overwrite create method

    def create(self, validated_data):
        product_id = self.context["product_id"]
        return Review.objects.create(product_id=product_id, **validated_data)


class CustomerSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Customer
        fields = ["id", "user_id", "phone", "birth_date", "membership"]
