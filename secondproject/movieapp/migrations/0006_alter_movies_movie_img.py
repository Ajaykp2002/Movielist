# Generated by Django 4.0.6 on 2022-08-16 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0005_rename_movie_movies'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='Movie_Img',
            field=models.ImageField(upload_to='new'),
        ),
    ]