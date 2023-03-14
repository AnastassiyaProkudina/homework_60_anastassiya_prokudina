from django.core.validators import MinValueValidator
from django.db import models

from online_store.manager import CartManager


class Cart(models.Model):
    product = models.ForeignKey(
        to="online_store.Product",
        related_name="carts",
        blank=False,
        on_delete=models.CASCADE,
        verbose_name="Product",
    )
    qty = models.IntegerField(
        null=False,
        blank=False,
        verbose_name="Quantity",
        validators=[MinValueValidator(0)],
        default=1,
    )

    def __str__(self):
        return f"{self.product} - {self.qty}"

    objects = CartManager()
