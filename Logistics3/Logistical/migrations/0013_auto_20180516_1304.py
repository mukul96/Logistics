# Generated by Django 2.0.4 on 2018-05-16 13:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Logistical', '0012_auto_20180516_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='invoice_date',
            field=models.DateField(default=datetime.datetime(2018, 5, 16, 13, 4, 32, 331273)),
        ),
        migrations.AlterField(
            model_name='orders',
            name='payment_due',
            field=models.DateField(default=datetime.datetime(2018, 5, 16, 13, 4, 32, 331300)),
        ),
        migrations.AlterField(
            model_name='pod',
            name='loading_date',
            field=models.DateField(default=datetime.datetime(2018, 5, 16, 13, 4, 32, 332305)),
        ),
        migrations.AlterField(
            model_name='pod',
            name='payment_date',
            field=models.DateField(default=datetime.datetime(2018, 5, 16, 13, 4, 32, 332407)),
        ),
        migrations.AlterField(
            model_name='pod',
            name='pod_receiving_date',
            field=models.DateField(default=datetime.datetime(2018, 5, 16, 13, 4, 32, 332278)),
        ),
        migrations.AlterField(
            model_name='suppliers',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='suppliers',
            name='alternate_number',
            field=models.IntegerField(blank=True, default=models.IntegerField(), null=True),
        ),
        migrations.AlterField(
            model_name='suppliers',
            name='no_own_vehicles',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
        migrations.AlterField(
            model_name='suppliers',
            name='pan_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
