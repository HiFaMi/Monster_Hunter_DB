# Generated by Django 2.1.2 on 2018-10-09 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('weapon', '0011_heavybowgun'),
        ('armor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accessory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slot_lv', models.CharField(max_length=50)),
                ('rare', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('armor', models.ManyToManyField(null=True, related_name='makes_armor', to='armor.Armor')),
                ('charge_blade', models.ManyToManyField(null=True, related_name='makes_charge_blade', to='weapon.ChargeBlade')),
                ('great_sword', models.ManyToManyField(null=True, related_name='makes_great_sword', to='weapon.GreatSword')),
                ('gun_lance', models.ManyToManyField(null=True, related_name='makes_gun_lance', to='weapon.GunLance')),
                ('hammer', models.ManyToManyField(null=True, related_name='makes_hammer', to='weapon.Hammer')),
                ('heavy_bowgun', models.ManyToManyField(null=True, related_name='makes_heavy_bowgun', to='weapon.HeavyBowgun')),
                ('lance', models.ManyToManyField(null=True, related_name='makes_lance', to='weapon.Lance')),
                ('light_bowgun', models.ManyToManyField(null=True, related_name='makes_light_bowgun', to='weapon.LightBowgun')),
                ('long_sword', models.ManyToManyField(null=True, related_name='makes_long_sword', to='weapon.LongSword')),
                ('one_hand_sword', models.ManyToManyField(null=True, related_name='makes_one_hand_sword', to='weapon.OneHandSword')),
                ('switch_axe', models.ManyToManyField(null=True, related_name='makes_switch_axe', to='weapon.SwitchAxe')),
                ('two_sowrds', models.ManyToManyField(null=True, related_name='makes_two_swords', to='weapon.TwoSwords')),
            ],
        ),
    ]