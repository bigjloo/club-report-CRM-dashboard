# Generated by Django 3.0.6 on 2020-05-06 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agents', '0002_club_platform'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='rakeback',
            field=models.DecimalField(decimal_places=3, max_digits=3),
        ),
    ]