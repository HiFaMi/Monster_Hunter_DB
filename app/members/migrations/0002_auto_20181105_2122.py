# Generated by Django 2.1.3 on 2018-11-05 12:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='create_date',
            new_name='create_at',
        ),
    ]
