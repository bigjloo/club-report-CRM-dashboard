# Generated by Django 3.0.6 on 2020-05-16 06:36

from decimal import Decimal
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agents', '0007_auto_20200514_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountclub',
            name='rakeback_percentage',
            field=models.DecimalField(decimal_places=3, max_digits=3, validators=[django.core.validators.MinValueValidator(Decimal('0.0'))]),
        ),
    ]