# Generated by Django 4.1.2 on 2022-11-08 14:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_catering_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='catering',
            old_name='email',
            new_name='emailmanu',
        ),
        migrations.RenameField(
            model_name='catering',
            old_name='name',
            new_name='namemanu',
        ),
        migrations.RenameField(
            model_name='catering',
            old_name='price',
            new_name='pricemanu',
        ),
    ]
