# Generated by Django 2.2.12 on 2023-11-24 21:05

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('cameras_listeners', '0023_auto_20231124_2200'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='cameras',
        ),
        migrations.AddField(
            model_name='player',
            name='cameras_off',
            field=otree.db.models.LongStringField(null=True, verbose_name='The cameras were off during this meeting. How did it affect your experience, including your ability to follow the talk?'),
        ),
        migrations.AddField(
            model_name='player',
            name='cameras_on',
            field=otree.db.models.LongStringField(null=True, verbose_name='The cameras were on during this meeting. How did it affect your experience, including your ability to follow the talk?'),
        ),
    ]
