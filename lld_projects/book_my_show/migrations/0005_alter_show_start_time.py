# Generated by Django 4.1.5 on 2023-01-09 15:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('book_my_show', '0004_remove_seat_screen_seat_screen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='start_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
