# Generated by Django 2.2.12 on 2023-11-24 20:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cameras_listeners', '0007_auto_20231124_2116'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='game_finished',
        ),
    ]
