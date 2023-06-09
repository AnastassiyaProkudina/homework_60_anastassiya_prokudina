# Generated by Django 4.1.7 on 2023-03-13 20:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('online_store', '0006_rename_productincart_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carts', to='online_store.product', verbose_name='Product'),
        ),
    ]
