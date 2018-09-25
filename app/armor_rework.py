import openpyxl

wb = openpyxl.load_workbook('armor_list.xlsx')
ws = wb['Armor']


for i in range(1, 755):
    base = ws.cell(row=i, column=6).value
    if base[2] is not '-':
        ws.cell(row=i, column=7).value = base[2]
    else:
        ws.cell(row=i, column=7).value = base[2:4]

    if base[2] is not '-':
        ws.cell(row=i, column=7).value = base[2]
    else:
        ws.cell(row=i, column=7).value = base[2:4]

wb.save('armor_list.xlsx')
print('Rework Done')


