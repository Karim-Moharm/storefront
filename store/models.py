from django.db import models


class Collection(models.Model):
    title = models.CharField(max_length=255)
    featured_product = models.ForeignKey(
        "Product", on_delete=models.SET_NULL, null=True, related_name="+"
    )


class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    invertory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    # PROTECT -> Prevents deleting the parent (Collection) if children (Product) exist .
    Collection = models.ForeignKey(Collection, on_delete=models.PROTECT)
    promotions = models.ManyToManyField(Promotion)

    class Meta:
        verbose_name = "Store Product - from Meta"
        verbose_name_plural = "store products - from Meta"


class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    birth_date = models.DateField(null=True, blank=True)
    membership = models.CharField(
        max_length=1,
        choices=[
            ("B", "Bronze"),
            ("S", "Silver"),
            ("G", "Gold"),
        ],
        default="B",
    )


class Order(models.Model):
    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(
        max_length=1,
        choices=[("P", "Pending"), ("C", "Complete"), ("F", "Failed")],
        default="P",
    )
    # the customer can have multiple orders, but the order belongs to one customer
    # so it's one to many rel
    # so the order table will have the customer foreign key
    # PROECT -> because you don't want to deleted an order from the data base even if the customr is deleted
    # but it will prevent deleting users who have order?????
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    """
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    """


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)


class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=30)
    # the relation between the customer and the address is one to one
    customer = models.OneToOneField(
        Customer, on_delete=models.CASCADE, primary_key=True
    )
    zip_code = models.CharField(max_length=20, null=True)

    # incase of one to many relation between customer and address
    # the customer can have many address
    # Address table will have a customer_id foreign key.
    """customer = models.ForeignKey(Customer, on_delete=models.CASCADE)"""


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
