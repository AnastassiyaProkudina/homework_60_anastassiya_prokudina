from django.core.validators import MinValueValidator
from django.db import models


class ProductInCart(models.Model):
    product = models.ForeignKey(
        to="online_store.Product",
        related_name='Product',
        blank=False,
        on_delete=models.PROTECT,
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
