import openpyxl

wb = openpyxl.load_workbook('armor_list.xlsx')
ws = wb['Armor']


def replace_multiple(main_string, to_be_replaces, new_string):
    for elem in to_be_replaces:
        if elem in main_string:
            main_string = main_string.replace(elem, new_string)
    return main_string


for i in range(1, 144):
    base = ws.cell(row=i, column=6).value
    ws.cell(row=i, column=7).value = replace_multiple(base, ['화', '수', '뇌', '빙', '용'], '')


wb.save('armor_list.xlsx')
print('Rework Done')
