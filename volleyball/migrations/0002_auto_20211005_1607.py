# Generated by Django 3.2.7 on 2021-10-05 12:37

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('volleyball', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='available_seats',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 10, 5, 12, 37, 11, 507462, tzinfo=utc)),
        ),
    ]
