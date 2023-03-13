from django.core.validators import MinValueValidator
from django.db import models
from django.db.models import TextChoices
from django.utils import timezone


class CategoryChoice(TextChoices):
    OTHER = "other", "Other"
    FOOD = "food", "Food"
    PHARMACY = "pharmacy", "Pharmacy"
    CAR = "car", "Car"
    DEVICE = "device", "Device"


class Product(models.Model):
    title = models.CharField(
        max_length=100, null=False, blank=False, verbose_name="Title"
    )
    description = models.TextField(
        max_length=2000,
        null=True,
        blank=False,
        verbose_name="Description",
        default="No Description",
    )
    image = models.TextField(
        max_length=2000, null=False, blank=False, verbose_name="Image"
    )
    category = models.TextField(
        max_length=40,
        choices=CategoryChoice.choices,
        verbose_name="Category",
        default=CategoryChoice.OTHER,
    )
    balance = models.IntegerField(
        null=False,
        blank=False,
        verbose_name="Balance",
        validators=[MinValueValidator(0)],
        default=None,
    )
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Price")
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Date and time created"
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Date and time updated"
    )
    is_deleted = models.BooleanField(verbose_name="Deleted", null=False, default=False)
    deleted_at = models.DateTimeField(
        verbose_name="Date and time deleted at", null=True, default=None
    )

    def __str__(self):
        return self.title

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()
