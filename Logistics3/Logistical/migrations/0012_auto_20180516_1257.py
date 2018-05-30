# Generated by Django 2.0.4 on 2018-05-16 12:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Logistical', '0011_auto_20180516_1232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='address_1',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customers',
            name='address_2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customers',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='customers',
            name='postal_code',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customers',
            name='website',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='invoice_date',
            field=models.DateField(default=datetime.datetime(2018, 5, 16, 12, 57, 55, 29406)),
        ),
        migrations.AlterField(
            model_name='orders',
            name='payment_due',
            field=models.DateField(default=datetime.datetime(2018, 5, 16, 12, 57, 55, 29434)),
        ),
        migrations.AlterField(
            model_name='pod',
            name='loading_date',
            field=models.DateField(default=datetime.datetime(2018, 5, 16, 12, 57, 55, 30436)),
        ),
        migrations.AlterField(
            model_name='pod',
            name='payment_date',
            field=models.DateField(default=datetime.datetime(2018, 5, 16, 12, 57, 55, 30538)),
        ),
        migrations.AlterField(
            model_name='pod',
            name='pod_receiving_date',
            field=models.DateField(default=datetime.datetime(2018, 5, 16, 12, 57, 55, 30410)),
        ),
    ]
