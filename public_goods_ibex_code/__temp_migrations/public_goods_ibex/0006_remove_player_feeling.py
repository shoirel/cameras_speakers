# Generated by Django 2.2.12 on 2023-06-17 08:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('public_goods_ibex', '0005_auto_20230617_1049'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='feeling',
        ),
    ]