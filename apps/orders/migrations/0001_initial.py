# Generated by Django 4.2.2 on 2024-06-02 18:58

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inventory', '0002_alter_inventory_options'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0002_address_role_remove_user_name_user_username_profile_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('is_active', models.BooleanField(default=True)),
                ('ordered', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[('D', 'Draft'), ('PE', 'Pending'), ('PC', 'Payment Complete'), ('IND', 'in-delivery'), ('CP', 'complete'), ('CN', 'cancelled')], default='D', max_length=3)),
                ('delivery_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('order_date', models.DateTimeField()),
                ('delivery_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.address')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('is_active', models.BooleanField(default=True)),
                ('status', models.CharField(choices=[('PE', 'Pending'), ('PA', 'Paid'), ('RE', 'Refunded'), ('FA', 'Failed'), ('CA', 'Cancelled')], default='PE', max_length=2)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_date', models.DateTimeField(default=datetime.datetime.now)),
                ('payment_method', models.CharField(choices=[('CA', 'Cash'), ('MO', 'Momo'), ('CD', 'Card'), ('SP', 'St_points'), ('RP', 'Referral_points')], default='CD', max_length=2)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('is_active', models.BooleanField(default=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.IntegerField()),
                ('inventory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.inventory')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.order')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='order',
            name='transaction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.transaction'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
