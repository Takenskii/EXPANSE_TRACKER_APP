# Generated by Django 5.1.5 on 2025-02-03 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currentbalance',
            name='current_balance',
            field=models.FloatField(),
        ),
    ]
