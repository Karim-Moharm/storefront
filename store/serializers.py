from rest_framework import serializers
from .models import Product, Collection, Order, Review, Customer, OrderItem
from decimal import Decimal
from carts.models import Cart, CartItem
from django.db import transaction



class CollectionTestSerializer(serializers.ModelSerializer):
    num_of_products = serializers.SerializerMethodField(method_name='products_count')
    class Meta:
        model = Collection
        fields = ['id', 'title', 'featured_product', "num_of_products"]

    def products_count(self, collection: Collection):
        return collection.product_set.count()


class ProductTestSerializer(serializers.ModelSerializer):
    price_with_tax = serializers.SerializerMethodField('calc_tax')

    def calc_tax(self, product: Product):
        return product.price * Decimal(1.1)
    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'price', 'price_with_tax', 'inventory', 'collection']

    def create(self, validated_data):
        return super().create(validated_data)


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


class CreateOrderSerializer(serializers.Serializer):
    cart_id = serializers.UUIDField()

    def save(self, **kwargs):
        with transaction.atomic():
            # get the customer_id from the user_id
            (customer, created) = Customer.objects.get_or_create(
                user_id=self.context["user_id"]
            )
            # creating an order using customer_id
            order = Order.objects.create(customer=customer)
            # getting the cartitems
            cart_items = CartItem.objects.select_related("productitem").filter(
                cart_id=self.validated_data["cart_id"]
            )

            # convert cart_items into order items
            # [item for items in collection]
            order_items = [
                OrderItem(
                    order=order,
                    product=item.product,
                    prrice=item.product.price,
                    quantity=item.quantity,
                )
                for item in cart_items
            ]
            OrderItem.objects.bulk_create(order_items)
            # delete th cart
            Cart.objects.filter(pk=self.validated_data["cart_id"])


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
