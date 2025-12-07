from django.db import models

# Create your models here.


class Order(models.Model):
    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(
        max_length=1,
        choices=[("P", "Pending"), ("C", "Complete"), ("F", "Failed")],
        default="P",
    )
