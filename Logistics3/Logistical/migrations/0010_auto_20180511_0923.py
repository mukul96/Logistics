# Generated by Django 2.0.4 on 2018-05-11 09:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Logistical', '0009_auto_20180510_0722'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pod_receiving_date', models.DateField(default=datetime.datetime(2018, 5, 11, 9, 23, 57, 281696))),
                ('loading_date', models.DateField(default=datetime.datetime(2018, 5, 11, 9, 23, 57, 281723))),
                ('lr_number', models.IntegerField()),
                ('truck_number', models.CharField(max_length=512)),
                ('receiver_name', models.CharField(max_length=512)),
                ('receiver_account_number', models.CharField(max_length=512)),
                ('bank_name', models.CharField(max_length=512)),
                ('amount', models.IntegerField()),
                ('payment_date', models.DateField(default=datetime.datetime(2018, 5, 11, 9, 23, 57, 281823))),
                ('remarks', models.TextField(blank=True, null=True)),
                ('consignor_name', models.CharField(max_length=512)),
            ],
        ),
        migrations.AlterField(
            model_name='orders',
            name='invoice_date',
            field=models.DateField(default=datetime.datetime(2018, 5, 11, 9, 23, 57, 280784)),
        ),
        migrations.AlterField(
            model_name='orders',
            name='payment_due',
            field=models.DateField(default=datetime.datetime(2018, 5, 11, 9, 23, 57, 280811)),
        ),
    ]
