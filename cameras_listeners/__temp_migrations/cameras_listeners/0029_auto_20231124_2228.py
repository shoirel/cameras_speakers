# Generated by Django 2.2.12 on 2023-11-24 21:28

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('cameras_listeners', '0028_auto_20231124_2228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='no_guess',
            field=otree.db.models.BooleanField(choices=[[True, 'I would like to guess the results now!'], [False, 'No more questions, please, just tell me what it’s about!']], default=True, null=True, verbose_name='<p></p><span style="line-height:1.7;font-size:30px"></span>Do you want to continue?'),
        ),
    ]