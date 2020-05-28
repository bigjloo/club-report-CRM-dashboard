# Generated by Django 3.0.6 on 2020-05-28 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agents', '0019_auto_20200526_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='platform',
            field=models.CharField(choices=[('UP', 'Upoker'), ('PB', 'PokerBros'), ('PPP', 'PPPoker'), ('ANP', 'All New Poker'), ('PT', 'PokerTime'), ('PM', 'PokerMaster')], default='PB', max_length=3),
        ),
    ]
