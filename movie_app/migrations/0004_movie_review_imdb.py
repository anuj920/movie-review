# Generated by Django 2.1.5 on 2019-05-19 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0003_auto_20190520_0056'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie_review',
            name='imdb',
            field=models.CharField(default=False, max_length=200),
        ),
    ]