# Generated by Django 4.0.6 on 2022-08-14 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0004_rename_img_movie_movie_img_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='movie',
            new_name='movies',
        ),
    ]
