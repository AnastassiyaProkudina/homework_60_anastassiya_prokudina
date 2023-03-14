from django.db import models


class Order(models.Model):
    product = models.ManyToManyField(
        to="online_store.Product",
        related_name="product",
        blank=True,
    )
    name = models.CharField(
        max_length=100, null=False, blank=False, verbose_name="Name"
    )
    phone = models.CharField(
        max_length=100, null=False, blank=False, verbose_name="Phone"
    )
    address = models.CharField(
        max_length=150, null=False, blank=False, verbose_name="address"
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Date and time created"
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Date and time updated"
    )

    def __str__(self):
        return self.name
