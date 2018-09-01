import os

import django
import openpyxl


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from weapon.models import GreatSword

wb = openpyxl.load_workbook('weapon_data.xlsx')

ws = wb['Great_Sword']


for row in range(2, 92):
        name = ws.cell(row=row, column=1).value
        rare = ws.cell(row=row, column=2).value
        produce = ws.cell(row=row, column=3).value
        attack = ws.cell(row=row, column=4).value
        defense = ws.cell(row=row, column=5).value
        if ws.cell(row=row, column=6).value is None:
            weapon_property = '없음'
            weapon_property_fiqure = '없음'
        else:
            weapon_property = ws.cell(row=row, column=6).value
            weapon_property_fiqure = ws.cell(row=row, column=7).value

        if ws.cell(row=row, column=8).value is None:
            abnormal_condition = '없음'
            abnormal_condition_figure = '없음'
        else:
            abnormal_condition = ws.cell(row=row, column=8).value
            abnormal_condition_figure = ws.cell(row=row, column=9).value

        fatal_blow = ws.cell(row=row, column=10).value
        if ws.cell(row=row, column=11).value is None:
            slot = '없음'
        else:
            slot = ws.cell(row=row, column=11).value
        # cost = ws.cell(row=row, column=12).value

        GreatSword.objects.create(
            name=name,
            rare=rare,
            produce=produce,
            attack=attack,
            defense=defense,
            weapon_property=weapon_property,
            weapon_property_fiqure=weapon_property_fiqure,
            abnormal_condition=abnormal_condition,
            abnormal_condition_figure=abnormal_condition_figure,
            fatal_blow=fatal_blow,
            slot=slot,
            # cost=cost
        )
print('Done')
