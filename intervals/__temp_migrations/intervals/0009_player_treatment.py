# Generated by Django 2.2.12 on 2023-09-30 12:30

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('intervals', '0008_auto_20230930_1338'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='treatment',
            field=otree.db.models.StringField(max_length=10000, null=True),
        ),
    ]
