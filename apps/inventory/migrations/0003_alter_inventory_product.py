# Generated by Django 4.2.2 on 2024-07-10 13:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0008_alter_productcategory_options"),
        ("inventory", "0002_alter_inventory_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="inventory",
            name="product",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to="products.product"
            ),
        ),
    ]
