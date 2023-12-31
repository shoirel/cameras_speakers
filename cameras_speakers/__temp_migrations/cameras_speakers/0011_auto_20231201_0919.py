# Generated by Django 2.2.12 on 2023-12-01 08:19

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('cameras_speakers', '0010_auto_20231201_0906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='assess1',
            field=otree.db.models.IntegerField(choices=[[0, '0 (This text does not summarise my project at all)'], [1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7 (This text is an excellent summary of my project)']], null=True, verbose_name='On a scale of 0 to 7, how would you assess this summary? Please note that this assessment <b>WILL NOT</b> be sent to the relevant Listener.'),
        ),
    ]
