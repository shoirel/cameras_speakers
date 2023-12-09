# Generated by Django 2.2.12 on 2023-11-24 22:28

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('cameras_listeners', '0064_auto_20231124_2327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='guess1',
            field=otree.db.models.IntegerField(choices=[[1, 'more than 15% higher when cameras are ON)'], [2, '5-15% higher when cameras are ON'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7 (way too difficult?)']], null=True, verbose_name=''),
        ),
    ]
