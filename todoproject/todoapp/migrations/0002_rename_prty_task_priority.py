# Generated by Django 4.1.4 on 2022-12-27 20:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='prty',
            new_name='priority',
        ),
    ]
