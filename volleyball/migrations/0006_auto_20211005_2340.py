# Generated by Django 3.2.7 on 2021-10-05 20:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('volleyball', '0005_alter_seat_transaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='seat',
            name='used',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='seat',
            name='transaction',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='volleyball.transaction'),
        ),
    ]
