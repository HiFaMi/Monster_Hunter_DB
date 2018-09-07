import os
import requests
from bs4 import BeautifulSoup
import openpyxl

url = 'http://mhf.inven.co.kr/dataninfo/mhw/armor/'

if not os.path.exists('data/armor_list.html'):
    armor_url = requests.get(url)
    with open('data/armor_list.html', 'wt') as f:
        f.write(armor_url.text)

with open('data/armor_list.html', 'rt') as f:
    html = f.read()


soup = BeautifulSoup(html, 'lxml')
code_list = soup.select('td.name.left > a')

wb = openpyxl.load_workbook('armor_list.xlsx')
ws = wb['Armor']

for code_index,code in enumerate(code_list):
    armor_detail_url = requests.get(url + code.get('href'))
    soup = BeautifulSoup(armor_detail_url.text, 'lxml')
    armor_detail_list = soup.select('div.mhw.armor_filter.armor_detail > table > tbody > tr > td')

    for armor_index, armor_detail in enumerate(armor_detail_list):
        ws.cell(row=code_index+1, column=armor_index+1).value = armor_detail.get_text(strip=True)

    print(armor_detail_list[0].get_text(strip=True) + ' Done')
wb.save('armor_list.xlsx')
print('Excel Done')


