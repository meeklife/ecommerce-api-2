# Generated by Django 4.2.2 on 2024-05-21 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productcategory',
            options={'ordering': ('created_at',)},
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
