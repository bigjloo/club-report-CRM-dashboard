# Generated by Django 3.0.6 on 2020-05-17 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting_engine', '0006_auto_20200516_1736'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='net_winloss',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='rakeback',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True),
        ),
    ]
