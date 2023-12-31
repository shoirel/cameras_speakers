# Generated by Django 2.2.12 on 2023-09-30 11:38

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('intervals', '0007_auto_20230930_1335'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='no_feedback',
            field=otree.db.models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], null=True, verbose_name='<span style="line-height:0.1;font-size:0.1px">and</span>'),
        ),
        migrations.AlterField(
            model_name='player',
            name='feedback',
            field=otree.db.models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], null=True, verbose_name='<span style="line-height:0.1;font-size:0.1px">and</span>'),
        ),
    ]
