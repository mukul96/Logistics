# Generated by Django 2.0.4 on 2018-05-16 12:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Logistical', '0010_auto_20180511_0923'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='freight',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='suppliers',
            name='type_of_supplier',
            field=models.CharField(default='manufacturer', max_length=512),
        ),
        migrations.AlterField(
            model_name='orders',
            name='invoice_date',
            field=models.DateField(default=datetime.datetime(2018, 5, 16, 12, 32, 50, 990585)),
        ),
        migrations.AlterField(
            model_name='orders',
            name='payment_due',
            field=models.DateField(default=datetime.datetime(2018, 5, 16, 12, 32, 50, 990613)),
        ),
        migrations.AlterField(
            model_name='pod',
            name='loading_date',
            field=models.DateField(default=datetime.datetime(2018, 5, 16, 12, 32, 50, 991657)),
        ),
        migrations.AlterField(
            model_name='pod',
            name='payment_date',
            field=models.DateField(default=datetime.datetime(2018, 5, 16, 12, 32, 50, 991756)),
        ),
        migrations.AlterField(
            model_name='pod',
            name='pod_receiving_date',
            field=models.DateField(default=datetime.datetime(2018, 5, 16, 12, 32, 50, 991631)),
        ),
        migrations.AlterField(
            model_name='suppliers',
            name='address',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='suppliers',
            name='alternate_number',
            field=models.IntegerField(blank=True, default=models.IntegerField()),
        ),
        migrations.AlterField(
            model_name='suppliers',
            name='no_own_vehicles',
            field=models.IntegerField(blank=True, default=1),
        ),
        migrations.AlterField(
            model_name='suppliers',
            name='pan_number',
            field=models.IntegerField(blank=True),
        ),
    ]
