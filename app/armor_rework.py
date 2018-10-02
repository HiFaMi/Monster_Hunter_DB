import openpyxl

wb = openpyxl.load_workbook('armor_list.xlsx')
ws = wb['Armor']


for i in range(1, 144):
    base = ws.cell(row=i, column=6).value
    skill_list = base.split('|')
    for index in range(len(skill_list)):
        ws.cell(row=i, column=7+index).value = skill_list[index]

wb.save('armor_list.xlsx')
print('Rework Done')
