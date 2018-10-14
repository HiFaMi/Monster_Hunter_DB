import openpyxl
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from armor.models.armor import Armor

wb = openpyxl.load_workbook('armor_list.xlsx')
ws = wb['Armor']

for index in range(1, 754):
    name = ws.cell(row=index, column=1).value
    equip_region = ws.cell(row=index, column=2).value
    rare = ws.cell(row=index, column=3).value
    cost = ws.cell(row=index, column=4).value
    defense = ws.cell(row=index, column=5).value
    vs_fire = ws.cell(row=index, column=7).value
    vs_water = ws.cell(row=index, column=8).value
    vs_thunder = ws.cell(row=index, column=9).value
    vs_ice = ws.cell(row=index, column=10).value
    vs_dragon = ws.cell(row=index, column=11).value
    slot = ws.cell(row=index, column=12).value

    Armor.objects.create(
        name=name,
        equip_region=equip_region,
        rare=rare,
        cost=cost,
        defense=defense,
        vs_fire=vs_fire,
        vs_water=vs_water,
        vs_thunder=vs_thunder,
        vs_ice=vs_ice,
        vs_dragon=vs_dragon,
        slot=slot,
    )

print('Armor Done')
