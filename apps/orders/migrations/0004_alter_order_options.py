# Generated by Django 4.2.2 on 2024-09-19 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_remove_order_transaction'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ('created_at',)},
        ),
    ]
