# Generated by Django 2.2.12 on 2023-11-24 20:14

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('cameras_listeners', '0005_auto_20231124_2106'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='game_finished',
            field=otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], null=True),
        ),
    ]
