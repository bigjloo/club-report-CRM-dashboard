# Generated by Django 3.0.6 on 2020-05-17 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting_engine', '0007_auto_20200517_1628'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='net_winloss_fiat',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True),
        ),
    ]
