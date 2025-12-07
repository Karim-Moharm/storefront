from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    invertory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)


class Customer(models.model):
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


class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=30)
    # the relation between the customer and the address is one to one
    customer = models.OneToOneField(
        Customer, on_delete=models.CASCADE, primary_key=True
    )

    # incase of one to many relation between customer and address
    """customer = models.ForeignKey(Customer, on_delete=models.CASCADE)"""
