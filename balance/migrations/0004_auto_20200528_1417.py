# Generated by Django 3.0.6 on 2020-05-28 06:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0006_remove_note_agent_player'),
        ('balance', '0003_auto_20200528_1240'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='balancesheet',
            name='notes',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='notes',
        ),
        migrations.AddField(
            model_name='balancesheet',
            name='note',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='notes.Note'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='note',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='notes.Note'),
        ),
    ]
