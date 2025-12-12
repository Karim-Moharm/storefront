from django.db import models
from django.core.validators import MinValueValidator
from django.conf import settings
from django.contrib import admin


class Collection(models.Model):
    title = models.CharField(max_length=255)
    featured_product = models.ForeignKey(
        "Product", on_delete=models.SET_NULL, null=True, related_name="+"
    )

    def __str__(self) -> str:
        return f"{self.title}"

    class Meta:
        ordering = ["title"]


class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()

    # def __str__(self):
    #     return f"{self.description} - {self.discount}"

    def __str__(self):
        return f"{self.description}"


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    slug = models.SlugField()
    price = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(1)]
    )
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    # PROTECT -> Prevents deleting the parent (Collection) if children (Product) exist .
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT)
    promotions = models.ManyToManyField(Promotion, blank=True)

    class Meta:
        verbose_name = "Store Product - from Meta"
        verbose_name_plural = "store products - from Meta"


class Customer(models.Model):
    MEMBERSHIP = [
        ("B", "Bronze"),
        ("S", "Silver"),
        ("G", "Gold"),
    ]
    phone = models.CharField(max_length=20)
    birth_date = models.DateField(null=True, blank=True)
    membership = models.CharField(
        max_length=1,
        choices=MEMBERSHIP,
        default="B",
    )
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    @admin.display(ordering="user__first_name")
    def first_name(self):
        return self.user.first_name

    @admin.display(ordering="user__last_name")
    def last_name(self):
        return self.user.last_name

    def email(self):
        return self.user.email

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} {self.membership}"

    class Meta:
        ordering = ["user__first_name"]


class Order(models.Model):
    # auto_now_add -> first time created
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

    """the correct????????
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    """


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.order.customer.first_name} {self.product} {self.quantity}"


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


class Review(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="reviews"
    )
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateField(auto_now_add=True)
