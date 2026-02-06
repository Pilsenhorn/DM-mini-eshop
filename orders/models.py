from django.db import models
from django.conf import settings
from products.models import Product

class Order(models.Model):
    CREATED = "created"
    PAID = "paid"
    PROCESSING = "processing"
    COMPLETED = "completed"
    CANCELED = "canceled"

    STATUS_CHOICES = [
        (CREATED, "Created"),
        (PAID, "Paid"),
        (PROCESSING, "Processing"),
        (COMPLETED, "Completed"),
        (CANCELED, "Canceled",)
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text="Registered user (optional)"
    )

    email = models.EmailField(
        help_text="Customer email (quest or user)"
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=CREATED
    )

    shipping_method = models.CharField(
        max_length=255,
        blank=True,
        help_text="Carrier or personal pickup"
    )

    shipping_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    note = models.TextField(
        blank=True,
        help_text="Customer note"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def is_paid(self):
        return self.status == self.PAID


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        related_name="itesm",
        on_delete=models.CASCADE
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT
    )

    quntity = models.PositiveBigIntegerField(default=1)

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text="Price at time of order"
    )

    def __str__(self):
        return f"{self.product.name} x {self.quntity}"