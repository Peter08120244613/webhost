# Generated by Django 4.2.1 on 2023-05-28 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='gen',
            new_name='gender',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='lev',
            new_name='level',
        ),
    ]
