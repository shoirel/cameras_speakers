# Generated by Django 2.2.12 on 2022-12-17 13:19

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('public_goods_ibex', '0002_auto_20221217_1414'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='individual_share_2',
            field=otree.db.models.CurrencyField(null=True),
        ),
        migrations.AddField(
            model_name='group',
            name='individual_share_3',
            field=otree.db.models.CurrencyField(null=True),
        ),
        migrations.AddField(
            model_name='group',
            name='total_contribution_2',
            field=otree.db.models.CurrencyField(null=True),
        ),
        migrations.AddField(
            model_name='group',
            name='total_contribution_3',
            field=otree.db.models.CurrencyField(null=True),
        ),
    ]
