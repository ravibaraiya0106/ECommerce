# Generated by Django 5.0 on 2023-12-28 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_alter_orders_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='amount',
            field=models.IntegerField(),
        ),
    ]
