# Generated by Django 4.1.5 on 2023-01-07 15:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parking_lot', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='parkingspot',
            name='lot_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='parking_lot.parkinglot'),
            preserve_default=False,
        ),
    ]
