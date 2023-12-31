# Generated by Django 2.2.12 on 2023-11-24 20:48

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('cameras_listeners', '0018_auto_20231124_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='knowledge',
            field=otree.db.models.IntegerField(choices=[[1, '1 (No prior knowledge)'], 2, 3, 4, 5, 6, [7, '7 (Expert prior knowledge)']], null=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='player',
            name='like',
            field=otree.db.models.IntegerField(choices=[[1, '1 (I certainly would not)'], 2, 3, 4, 5, 6, [7, '7 (I certainly would)']], null=True, verbose_name=''),
        ),
    ]
