# Generated by Django 4.1.2 on 2022-11-08 16:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_rename_musicalconcert_musicalconcertm'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Musicalconcertm',
        ),
        migrations.DeleteModel(
            name='weddinghalls',
        ),
    ]