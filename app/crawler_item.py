import requests
from bs4 import BeautifulSoup
import openpyxl

url = 'http://mhf.inven.co.kr/dataninfo/mhw/item/'

item_url = requests.get(url)
html = item_url.text

soup = BeautifulSoup(html, 'lxml')

code_list = soup.select('div.mhw.board > ul > li > a')

wb = wb = openpyxl.load_workbook('armor_list.xlsx')
ws = wb['Item']

# for code_index, code in enumerate(code_list):
#     item_detail_url = requests.get(url + code.get('href'))
#     soup = BeautifulSoup(item_detail_url.text, 'lxml')
#     print(code)
#     print(soup.select_one('tr > td.left').get_text(strip=True))

for index in range(len(code_list)):
    ws.cell(row=index+1, column=1).value = code_list[index].get_text(strip=True)
    print(code_list[index].get_text(strip=True) + ' Done')

wb.save('armor_list.xlsx')
print('all save')
