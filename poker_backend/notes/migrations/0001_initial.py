# Generated by Django 3.0.6 on 2020-05-20 12:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('agents', '0010_auto_20200520_2043'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField()),
                ('agent_player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='agents.AgentPlayer')),
            ],
        ),
    ]
