# Generated by Django 3.2.7 on 2021-10-05 12:00

import datetime
from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teamA', models.CharField(max_length=20)),
                ('teamB', models.CharField(max_length=20)),
                ('date', models.DateField()),
                ('available_seats', django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), size=None)),
                ('ticket_price', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Stadium',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('capacity', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TransAction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField()),
                ('date', models.DateField(default=datetime.datetime(2021, 10, 5, 12, 0, 41, 129832, tzinfo=utc))),
                ('success', models.BooleanField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.PositiveIntegerField()),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='volleyball.match')),
                ('transaction', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='volleyball.transaction')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='match',
            name='stadium',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='volleyball.stadium'),
        ),
    ]
