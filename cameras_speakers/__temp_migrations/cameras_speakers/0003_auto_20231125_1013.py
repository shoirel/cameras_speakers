# Generated by Django 2.2.12 on 2023-11-25 09:13

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('cameras_speakers', '0002_auto_20231125_1011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='rec_kept',
            field=otree.db.models.IntegerField(choices=[[1, 'Yes, I am OK with it'], [2, 'No, I want the recording to be deleted'], [3, 'I don’t know yet, please send me the recording before I decide']], null=True, verbose_name='<p><font color="#33CC33">Do you agree that the recording of your talk is kept, possibly to be shared within the Commission to promote your project? </font>It also means taking part in the competition for the best talk. If you give consent after each of your two performances, they will have an independent chance in the competition.</p> <p> Please note that if you choose “Yes”, we will also send you the recording</p>'),
        ),
    ]
