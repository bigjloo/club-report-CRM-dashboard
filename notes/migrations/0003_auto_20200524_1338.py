# Generated by Django 3.0.6 on 2020-05-24 05:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_auto_20200524_1326'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Annoucement',
            new_name='Announcement',
        ),
        migrations.RenameField(
            model_name='announcement',
            old_name='annoucement',
            new_name='announcement',
        ),
    ]