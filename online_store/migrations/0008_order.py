# Generated by Django 4.1.7 on 2023-03-14 09:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("online_store", "0007_alter_cart_product"),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="Name")),
                ("phone", models.CharField(max_length=100, verbose_name="Phone")),
                ("address", models.CharField(max_length=150, verbose_name="address")),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Date and time created"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Date and time updated"
                    ),
                ),
                (
                    "product",
                    models.ManyToManyField(
                        blank=True, related_name="product", to="online_store.product"
                    ),
                ),
            ],
        ),
    ]
