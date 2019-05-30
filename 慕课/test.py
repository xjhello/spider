import requests
from bs4 import BeautifulSoup
from lxml import etree

# 1. 将目标网站页面抓取
headers = {
    'User-Agent':
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36 ',
}




def spider(url):
    response = requests.get(url, headers=headers)
    text = response.content.decode('utf-8')
    soup = BeautifulSoup(text, 'lxml')
    div = soup.find('div', class_='bread-crumbs')  # 得到div
    aList = div.find_all('a')  # , href='/learn/qa/102.html'
    href = aList[1]['href']
    if href == '/learn/qa/102.html':
        print('!!!!!!!!!!!!'+url)
    else:
        print(href)
        print('.')

def main():
    url = 'https://coding.imooc.com/learn/questiondetail/{}.html'
    for i in range(18110, 11111111):
        new_url = url.format(i)
        spider(new_url)
        # print(new_url )


if __name__ == '__main__':
    main()

# with open('mooc.html', 'w',encoding='utf-8') as fp:
#     fp.write(text)
