# Generated by Django 2.1.5 on 2019-05-19 21:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0007_auto_20190520_0244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie_review',
            name='reviewrating',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)]),
        ),
    ]
