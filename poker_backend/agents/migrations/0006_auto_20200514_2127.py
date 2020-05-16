# Generated by Django 3.0.6 on 2020-05-14 13:27

from decimal import Decimal
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agents', '0005_auto_20200514_2006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='agent_players',
            field=models.ManyToManyField(blank=True, null=True, related_name='accounts', to='agents.AgentPlayer'),
        ),
        migrations.AlterField(
            model_name='account',
            name='clubs',
            field=models.ManyToManyField(blank=True, null=True, related_name='accounts', through='agents.AccountClub', to='agents.Club'),
        ),
        migrations.AlterField(
            model_name='accountclub',
            name='chip_value',
            field=models.DecimalField(decimal_places=2, max_digits=5, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))]),
        ),
    ]
