# Generated by Django 2.2.12 on 2023-11-25 08:13

from django.db import migrations, models
import django.db.models.deletion
import otree.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('otree', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_in_subsession', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cameras_speakers_group', to='otree.Session')),
            ],
            options={
                'db_table': 'cameras_speakers_group',
            },
        ),
        migrations.CreateModel(
            name='Subsession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('session', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cameras_speakers_subsession', to='otree.Session')),
            ],
            options={
                'db_table': 'cameras_speakers_subsession',
            },
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_in_group', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('_payoff', otree.db.models.CurrencyField(default=0, null=True)),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('_gbat_is_waiting', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False, null=True)),
                ('_gbat_grouped', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False, null=True)),
                ('TREATMENT', otree.db.models.StringField(max_length=10000, null=True)),
                ('summary', otree.db.models.LongStringField(max_length=2000, null=True, verbose_name='')),
                ('familiar', otree.db.models.IntegerField(choices=[[1, 'Yes'], [2, 'No'], [3, 'Not Sure']], null=True, verbose_name='Had you known this project before?')),
                ('knowledge', otree.db.models.IntegerField(choices=[[1, '1 (No prior knowledge)'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7 (Expert prior knowledge)']], null=True, verbose_name='How would you assess your knowledge of the topic, prior to the talk?')),
                ('like', otree.db.models.IntegerField(choices=[[1, '1 (I certainly would not)'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7 (I certainly would)']], null=True, verbose_name='Would you like to learn more about the project?')),
                ('enjoy', otree.db.models.IntegerField(choices=[[1, '1 (Not at all)'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7 (Very much)']], null=True, verbose_name='How much did you enjoy the presentation?')),
                ('clarity', otree.db.models.IntegerField(choices=[[1, '1 (Not clear at all)'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7 (Completely clear)']], null=True, verbose_name='Would you like to learn more about the project?')),
                ('connection', otree.db.models.IntegerField(choices=[[1, '1 (Not at all)'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7 (Very well)']], null=True, verbose_name='Do you think the speaker could connect well with the audience?')),
                ('easiness', otree.db.models.IntegerField(choices=[[1, '1 (way too easy?)'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7 (way too difficult?)']], null=True, verbose_name='For you, was the presentation...')),
                ('cameras_on', otree.db.models.LongStringField(null=True, verbose_name='The cameras were on during this meeting. How did it affect your experience, including your ability to follow the talk?')),
                ('cameras_off', otree.db.models.LongStringField(null=True, verbose_name='The cameras were off during this meeting. How did it affect your experience, including your ability to follow the talk?')),
                ('remarks', otree.db.models.LongStringField(null=True, verbose_name='Any further remarks, reflections on your experience as a Listener or specific suggestions for the Speaker?')),
                ('no_guess', otree.db.models.BooleanField(choices=[[True, 'I would like to guess the results now!'], [False, 'No thanks, I’m done!']], default=True, null=True, verbose_name='<span style="line-height:1.7;font-size:25px"><font color="#33CC33">Do you want to continue?</font></span>')),
                ('cameras_good', otree.db.models.LongStringField(blank=True, null=True, verbose_name='')),
                ('guess1', otree.db.models.IntegerField(choices=[[1, 'more than 15% higher when cameras are ON'], [2, '5-15% higher when cameras are ON'], [3, 'about the same'], [4, '5-15% higher when cameras are OFF'], [5, 'more than 15% higher when cameras are OFF']], null=True, verbose_name='')),
                ('guess2', otree.db.models.IntegerField(choices=[[1, 'more than 15% higher when cameras are ON'], [2, '5-15% higher when cameras are ON'], [3, 'about the same'], [4, '5-15% higher when cameras are OFF'], [5, 'more than 15% higher when cameras are OFF']], null=True, verbose_name='')),
                ('guess3', otree.db.models.IntegerField(choices=[[1, 'more than 15% higher when cameras are ON'], [2, '5-15% higher when cameras are ON'], [3, 'about the same'], [4, '5-15% higher when cameras are OFF'], [5, 'more than 15% higher when cameras are OFF']], null=True, verbose_name='')),
                ('guess4', otree.db.models.IntegerField(choices=[[1, 'more than 15% higher when cameras are ON'], [2, '5-15% higher when cameras are ON'], [3, 'about the same'], [4, '5-15% higher when cameras are OFF'], [5, 'more than 15% higher when cameras are OFF']], null=True, verbose_name='')),
                ('guess5', otree.db.models.IntegerField(choices=[[1, 'more than 15% higher when cameras are ON'], [2, '5-15% higher when cameras are ON'], [3, 'about the same'], [4, '5-15% higher when cameras are OFF'], [5, 'more than 15% higher when cameras are OFF']], null=True, verbose_name='')),
                ('guess1_reversed', otree.db.models.IntegerField(choices=[[1, 'more than 15% higher when cameras are OFF'], [2, '5-15% higher when cameras are OFF'], [3, 'about the same'], [4, '5-15% higher when cameras are ON'], [5, 'more than 15% higher when cameras are ON']], null=True, verbose_name='')),
                ('guess2_reversed', otree.db.models.IntegerField(choices=[[1, 'more than 15% higher when cameras are OFF'], [2, '5-15% higher when cameras are OFF'], [3, 'about the same'], [4, '5-15% higher when cameras are ON'], [5, 'more than 15% higher when cameras are ON']], null=True, verbose_name='')),
                ('guess3_reversed', otree.db.models.IntegerField(choices=[[1, 'more than 15% higher when cameras are OFF'], [2, '5-15% higher when cameras are OFF'], [3, 'about the same'], [4, '5-15% higher when cameras are ON'], [5, 'more than 15% higher when cameras are ON']], null=True, verbose_name='')),
                ('guess4_reversed', otree.db.models.IntegerField(choices=[[1, 'more than 15% higher when cameras are OFF'], [2, '5-15% higher when cameras are OFF'], [3, 'about the same'], [4, '5-15% higher when cameras are ON'], [5, 'more than 15% higher when cameras are ON']], null=True, verbose_name='')),
                ('guess5_reversed', otree.db.models.IntegerField(choices=[[1, 'more than 15% higher when cameras are OFF'], [2, '5-15% higher when cameras are OFF'], [3, 'about the same'], [4, '5-15% higher when cameras are ON'], [5, 'more than 15% higher when cameras are ON']], null=True, verbose_name='')),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cameras_speakers.Group')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cameras_speakers_player', to='otree.Participant')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cameras_speakers_player', to='otree.Session')),
                ('subsession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cameras_speakers.Subsession')),
            ],
            options={
                'db_table': 'cameras_speakers_player',
            },
        ),
        migrations.AddField(
            model_name='group',
            name='subsession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cameras_speakers.Subsession'),
        ),
    ]
