# Generated by Django 2.2.12 on 2023-12-01 10:39

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('cameras_listeners', '0069_auto_20231124_2356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='clarity',
            field=otree.db.models.IntegerField(choices=[[0, '(Not clear at all) 0'], [1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7 (Completely clear)']], null=True, verbose_name='How clear was the presentation?'),
        ),
        migrations.AlterField(
            model_name='player',
            name='connection',
            field=otree.db.models.IntegerField(choices=[[0, '(Not at all) 0'], [1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7 (Very well)']], null=True, verbose_name='Do you think the speaker could connect well with the audience?'),
        ),
        migrations.AlterField(
            model_name='player',
            name='easiness',
            field=otree.db.models.IntegerField(choices=[[-3, '(way too difficult?) -3'], [-2, '-2'], [-1, '-1'], [0, '0'], [1, '1'], [2, '2'], [3, '3 (way too easy?)']], null=True, verbose_name='For you, was the presentation...'),
        ),
        migrations.AlterField(
            model_name='player',
            name='enjoy',
            field=otree.db.models.IntegerField(choices=[[0, '(Not at all) 0'], [1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7 (Very much)']], null=True, verbose_name='How much did you enjoy the presentation?'),
        ),
        migrations.AlterField(
            model_name='player',
            name='knowledge',
            field=otree.db.models.IntegerField(choices=[[0, '(No prior knowledge) 0'], [1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7 (Expert prior knowledge)']], null=True, verbose_name='How would you assess your knowledge of the topic, prior to the talk?'),
        ),
        migrations.AlterField(
            model_name='player',
            name='like',
            field=otree.db.models.IntegerField(choices=[[0, '(I certainly would not) 0'], [1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7 (I certainly would)']], null=True, verbose_name='Would you like to learn more about the project?'),
        ),
    ]
