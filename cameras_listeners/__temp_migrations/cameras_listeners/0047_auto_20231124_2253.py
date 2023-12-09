# Generated by Django 2.2.12 on 2023-11-24 21:53

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('cameras_listeners', '0046_auto_20231124_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='no_guess',
            field=otree.db.models.BooleanField(choices=[[True, 'I would like to guess the results now!'], [False, 'No thanks, I’m done!']], default=True, null=True, verbose_name='<span style="line-height:1.7;font-size:30px">Do you want to continue?</span><span style="font-size:1px">b.:</span>'),
        ),
    ]
