# Generated by Django 3.0.6 on 2020-05-11 08:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('agents', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gross_winloss', models.DecimalField(decimal_places=2, max_digits=7)),
                ('total_rake', models.DecimalField(decimal_places=2, max_digits=7)),
                ('rakeback_earnings', models.DecimalField(decimal_places=2, max_digits=7)),
                ('net_winloss', models.DecimalField(decimal_places=2, max_digits=7)),
                ('insurance', models.DecimalField(blank=True, decimal_places=2, max_digits=7)),
                ('jackpot', models.DecimalField(blank=True, decimal_places=2, max_digits=7)),
                ('hands', models.IntegerField(blank=True)),
                ('created', models.DateField(auto_now_add=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reports', to='agents.AgentPlayer')),
            ],
        ),
    ]