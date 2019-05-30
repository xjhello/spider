import requests
from lxml import etree
from bs4 import BeautifulSoup

# 全局变量
url = 'http://yjsc.shnu.edu.cn/79/d1/c17243a686545/page.htm'
HEADERS= {
    'User-Agent':
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36 '
}

# def spider():
response = requests.get(url, headers=HEADERS)
text = response.text
soup = BeautifulSoup(text, 'html5lib')
conMidtab = soup.find('table', class_='MsoNormalTable')  # 得到div
tables = conMidtab.find_all('tbody')

for table in tables:
    trs = table.find_all('tr')[2:]  # 过滤前两个
    print(trs)
#
# for tr in trs:
#     tds = tr.find_all('td')
#     # print(tds)
#     # profession = tds[0]
#     number = tds[1]
#     print(number.string)
    # if profession.string.startswith('04') and number.string.startswith('拟'):
    #     print(profession.string,number.string)


