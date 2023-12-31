# Generated by Django 2.2.12 on 2023-10-08 19:44

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('intervals', '0014_auto_20231007_1004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='germans_lower',
            field=otree.db.models.IntegerField(blank=True, null=True, verbose_name='<span style="line-height:1.7;font-size:18px">The European Commission has about 32,000 employees. How many of them are German native speakers?</span><span style="line-height:1.7;font-size:18px"><p><font color =\'green\'>Please answer in <b>absolute numbers</b>, not in terms of percentage of the total number of employees.</font></span><span style="line-height:1.7;font-size:18px"></p><p></p> I am 90% sure that the number is between</span>'),
        ),
    ]
