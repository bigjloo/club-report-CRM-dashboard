# Generated by Django 3.0.6 on 2020-05-16 09:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agents', '0008_auto_20200516_1436'),
        ('accounting_engine', '0003_auto_20200515_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='account',
            field=models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reports', to='agents.Account'),
        ),
        migrations.AlterField(
            model_name='report',
            name='agent_player',
            field=models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reports', to='agents.AgentPlayer'),
        ),
        migrations.AlterField(
            model_name='report',
            name='club',
            field=models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reports', to='agents.Club'),
        ),
        migrations.AlterField(
            model_name='report',
            name='hands',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='insurance',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='jackpot',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True),
        ),
    ]
