# Generated by Django 3.0.6 on 2020-05-28 03:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_auto_20200524_1338'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='agent_player',
        ),
    ]