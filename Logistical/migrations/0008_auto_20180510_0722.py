# Generated by Django 2.0.4 on 2018-05-10 07:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Logistical', '0007_auto_20180508_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='invoice_date',
            field=models.DateField(default=datetime.datetime(2018, 5, 10, 7, 22, 30, 820725)),
        ),
        migrations.AlterField(
            model_name='orders',
            name='payment_due',
            field=models.DateField(default=datetime.datetime(2018, 5, 10, 7, 22, 30, 820754)),
        ),
    ]
