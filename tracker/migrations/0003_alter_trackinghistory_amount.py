# Generated by Django 5.1.5 on 2025-02-03 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_alter_currentbalance_current_balance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trackinghistory',
            name='amount',
            field=models.FloatField(default=0.0),
        ),
    ]
