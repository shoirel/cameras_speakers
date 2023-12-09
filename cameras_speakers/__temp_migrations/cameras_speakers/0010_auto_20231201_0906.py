# Generated by Django 2.2.12 on 2023-12-01 08:06

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('cameras_speakers', '0009_auto_20231125_1028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='assess1',
            field=otree.db.models.IntegerField(choices=[[0, "(This text does not summarise my project at all) 0'"], [1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7 (This text is an excellent summary of my project)']], null=True, verbose_name='On a scale of 0 to 7, how would you assess this summary? Please note that this assessment <b>WILL NOT</b> be sent to the relevant Listener.'),
        ),
        migrations.AlterField(
            model_name='player',
            name='assess2',
            field=otree.db.models.IntegerField(choices=[[0, "(This text does not summarise my project at all) 0'"], [1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7 (This text is an excellent summary of my project)']], null=True, verbose_name='On a scale of 0 to 7, how would you assess this summary? Please note that this assessment <b>WILL NOT</b> be sent to the relevant Listener.'),
        ),
        migrations.AlterField(
            model_name='player',
            name='assess3',
            field=otree.db.models.IntegerField(choices=[[0, "(This text does not summarise my project at all) 0'"], [1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7 (This text is an excellent summary of my project)']], null=True, verbose_name='On a scale of 0 to 7, how would you assess this summary? Please note that this assessment <b>WILL NOT</b> be sent to the relevant Listener.'),
        ),
        migrations.AlterField(
            model_name='player',
            name='assess4',
            field=otree.db.models.IntegerField(choices=[[0, "(This text does not summarise my project at all) 0'"], [1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7 (This text is an excellent summary of my project)']], null=True, verbose_name='On a scale of 0 to 7, how would you assess this summary? Please note that this assessment <b>WILL NOT</b> be sent to the relevant Listener.'),
        ),
        migrations.AlterField(
            model_name='player',
            name='assess5',
            field=otree.db.models.IntegerField(choices=[[0, "(This text does not summarise my project at all) 0'"], [1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7 (This text is an excellent summary of my project)']], null=True, verbose_name='On a scale of 0 to 7, how would you assess this summary? Please note that this assessment <b>WILL NOT</b> be sent to the relevant Listener.'),
        ),
        migrations.AlterField(
            model_name='player',
            name='assess6',
            field=otree.db.models.IntegerField(choices=[[0, "(This text does not summarise my project at all) 0'"], [1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7 (This text is an excellent summary of my project)']], null=True, verbose_name='On a scale of 0 to 7, how would you assess this summary? Please note that this assessment <b>WILL NOT</b> be sent to the relevant Listener.'),
        ),
        migrations.AlterField(
            model_name='player',
            name='assess7',
            field=otree.db.models.IntegerField(choices=[[0, "(This text does not summarise my project at all) 0'"], [1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7 (This text is an excellent summary of my project)']], null=True, verbose_name='On a scale of 0 to 7, how would you assess this summary? Please note that this assessment <b>WILL NOT</b> be sent to the relevant Listener.'),
        ),
        migrations.AlterField(
            model_name='player',
            name='clarity',
            field=otree.db.models.IntegerField(choices=[[0, '(Not clear at all) 0'], [1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7 (Completely clear)']], null=True, verbose_name='How clear was the presentation?'),
        ),
        migrations.AlterField(
            model_name='player',
            name='connection',
            field=otree.db.models.IntegerField(choices=[[0, '(Not at all) 0'], [1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7 (Very well)']], null=True, verbose_name='Did they think you could connect well with the audience?'),
        ),
        migrations.AlterField(
            model_name='player',
            name='easiness',
            field=otree.db.models.IntegerField(choices=[[-3, '(way too difficult?) -3'], [-2, '-2'], [-1, '-1'], [0, '0'], [1, '1'], [2, '2'], [3, '3 (way too easy?)']], null=True, verbose_name='For them, was the presentation...'),
        ),
        migrations.AlterField(
            model_name='player',
            name='enjoy',
            field=otree.db.models.IntegerField(choices=[[0, '(Not at all) 0'], [1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7 (Very much)']], null=True, verbose_name='How much did they enjoy the presentation?'),
        ),
        migrations.AlterField(
            model_name='player',
            name='like',
            field=otree.db.models.IntegerField(choices=[[0, '(They certainly would not) 0'], [1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7 (They certainly would)']], null=True, verbose_name='Would they like to learn more about the project?'),
        ),
        migrations.AlterField(
            model_name='player',
            name='satisfied',
            field=otree.db.models.IntegerField(choices=[[1, '(Not at all satisfied) 1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7 (Fully satisfied)']], null=True, verbose_name='How satisfied are you with your talk?'),
        ),
    ]
