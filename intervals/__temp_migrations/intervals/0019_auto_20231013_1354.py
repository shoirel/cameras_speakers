# Generated by Django 2.2.12 on 2023-10-13 11:54

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('intervals', '0018_auto_20231013_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='assumed_one',
            field=otree.db.models.BooleanField(blank=True, choices=[[True, 'It did'], [False, 'It did not']], null=True),
        ),
    ]
