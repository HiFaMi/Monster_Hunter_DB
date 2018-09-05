# Generated by Django 2.1.1 on 2018-09-05 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weapon', '0008_switchaxe'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChargeBlade',
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
                ('phial_type', models.CharField(max_length=200)),
            ],
        ),
    ]
