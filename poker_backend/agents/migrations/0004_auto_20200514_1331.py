# Generated by Django 3.0.6 on 2020-05-14 05:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agents', '0003_auto_20200511_1709'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='agent_player',
            new_name='agent_players',
        ),
    ]
