# Generated by Django 3.0.6 on 2020-05-28 06:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0005_note_agent_player'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='agent_player',
        ),
    ]
