# Generated by Django 2.1.1 on 2018-09-03 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weapon', '0004_twoswords'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hammer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('rare', models.IntegerField()),
                ('produce', models.CharField(max_length=100)),
                ('attack', models.IntegerField()),
                ('defense', models.IntegerField()),
                ('weapon_property', models.CharField(max_length=100)),
                ('weapon_property_fiqure', models.CharField(max_length=100)),
                ('abnormal_condition', models.CharField(max_length=100)),
                ('abnormal_condition_figure', models.CharField(max_length=100)),
                ('fatal_blow', models.IntegerField()),
                ('slot', models.CharField(max_length=100)),
            ],
        ),
    ]
