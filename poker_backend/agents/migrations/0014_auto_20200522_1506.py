# Generated by Django 3.0.6 on 2020-05-22 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agents', '0013_auto_20200521_2321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='club_account_id',
            field=models.IntegerField(),
        ),
    ]
