from django.db import models

class Product(models.Model):
    DIGITAL = "digital"
    JEWELRY = "jewelry"
    SERVICE = "service"

    PRODUCT_TYPE_CHOICES = [
        (DIGITAL, "Digital product"),
        (JEWELRY, "Jewelry"),
        (SERVICE, "Service"),
    ]

    name = models.CharField(
        max_length=255,
        help_text="Product name show to customers"
    )

    descriptions = models.TextField(
        help_text="Detailed product description"
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text="Product price"
    )

    product_type = models.CharField(
        max_length=20,
        choices=PRODUCT_TYPE_CHOICES
    )

    is_active = models.BooleanField(
        default=True,
        help_text="Is product visible in shop"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updatet_at = models.DateTimeField(auto_now=True)

    # --- Digital product --- 

    digital_file = models.FileField(
        upload_to="digital_products/",
        blank=True,
        null=True,
        help_text="File available after payment"
    )

    def __str__(self):
        return f"{self.name} ({self.product_type})"
