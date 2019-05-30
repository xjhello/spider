import requests
import re
from lxml import etree
from bs4 import BeautifulSoup

names = [
    '人文与传播学院',
    '外国语学院',
    '教育学院',
    '音乐学院',
    '谢晋影视艺术学院',
    '商学院',
    '美术学院',
    '数理学院',
    '生命与环境科学学院',
    '旅游学院',
    '体育学院',
    '信息与机电工程学院',
    '哲学与法政学院',
    '对外汉语学院',
    '马克思主义学院',
    '教育硕士管理中心（筹）'
]
urls = [
    #人文与传播学院
    'http://yjsc.shnu.edu.cn/_upload/article/files/97/52/2d41568c431484d47e504356a2ed/8cd36e53-ca7c-404f-a024-5fedf9f3ab31.html',
    #外国语学院
    'http://yjsc.shnu.edu.cn/_upload/article/files/97/52/2d41568c431484d47e504356a2ed/ae380cfa-96a9-4170-a81e-e2caa9531ee1.html',
    #教育学院
    'http://yjsc.shnu.edu.cn/_upload/article/files/97/52/2d41568c431484d47e504356a2ed/e71fcc96-fa92-42be-b8af-323b7a8d5057.html',
    #音乐学院
    'http://yjsc.shnu.edu.cn/_upload/article/files/97/52/2d41568c431484d47e504356a2ed/50202703-6b26-43c0-9745-73adfa9b0dbd.html',
    #谢晋影视艺术学院
    'http://yjsc.shnu.edu.cn/_upload/article/files/97/52/2d41568c431484d47e504356a2ed/73deb1a2-4932-4db8-8a35-8c6ccbf12cd4.html',
    #商学院
    'http://yjsc.shnu.edu.cn/_upload/article/files/97/52/2d41568c431484d47e504356a2ed/9452c776-2e27-48e7-b16d-456cdbd0e0c1.html',
    #美术学院
    'http://yjsc.shnu.edu.cn/_upload/article/files/97/52/2d41568c431484d47e504356a2ed/02bb5c15-dd36-4cb5-9512-edc804d05bfa.html',
    #数理学院
    'http://yjsc.shnu.edu.cn/_upload/article/files/97/52/2d41568c431484d47e504356a2ed/6379da25-39fa-47cc-b988-fb9237d1e3b5.html',
    #生命与环境科学学院
    'http://yjsc.shnu.edu.cn/_upload/article/files/97/52/2d41568c431484d47e504356a2ed/083355a9-8839-4fd3-8b38-41b7f6765f5b.html',
    #旅游学院
    'http://yjsc.shnu.edu.cn/_upload/article/files/97/52/2d41568c431484d47e504356a2ed/91d7bbbd-a587-4852-85da-638996c2dbea.html',
    #体育学院
    'http://yjsc.shnu.edu.cn/_upload/article/files/97/52/2d41568c431484d47e504356a2ed/a04fd6b6-bf37-452a-ad23-321cd50f6455.html',
    #信息与机电工程学院
    'http://yjsc.shnu.edu.cn/_upload/article/files/97/52/2d41568c431484d47e504356a2ed/33cf9ae9-949c-4281-93ec-fee469b6b39e.html',
    #哲学与法政学院
    'http://yjsc.shnu.edu.cn/_upload/article/files/97/52/2d41568c431484d47e504356a2ed/d6cbc017-8287-40e4-b08a-c91760d126d0.html',
    #对外汉语学院
    'http://yjsc.shnu.edu.cn/_upload/article/files/97/52/2d41568c431484d47e504356a2ed/31b1d60c-affa-4f7e-a461-7dadad45fc6a.html',
    #马克思主义学院
    'http://yjsc.shnu.edu.cn/_upload/article/files/97/52/2d41568c431484d47e504356a2ed/61f44d7a-0cd7-47c4-9f49-789ca001f05d.html',
    #教育硕士管理中心（筹）
    'http://yjsc.shnu.edu.cn/_upload/article/files/97/52/2d41568c431484d47e504356a2ed/80c64b42-63cf-4745-90b6-4d165a44358b.html',

]
# 全局变量
a = []
url = 'http://yjsc.shnu.edu.cn/_upload/article/files/97/52/2d41568c431484d47e504356a2ed/e71fcc96-fa92-42be-b8af-323b7a8d5057.html'
HEADERS= {
    'User-Agent':
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36 '
}


# 爬取页面
def spider(url):
    response = requests.get(url, headers=HEADERS)
    text = response.text
    soup = BeautifulSoup(text, 'html5lib')
    conMidtab = soup.find('table', id='table11')  # 得到div
    tables = conMidtab.find_all('tbody')
    # print(len(tables))
    for table in tables:
        trs = table.find_all('tr')[2:]  # 过滤前两个
    for tr in trs:
        tds = tr.find_all('td')
        profession = tds[0].get_text()
        number = tds[1].get_text()
        ss = re.findall("\d+", profession)
        ss = ''.join(ss)
        if len(ss) > 4:
            s = re.findall("\d+", number)[0]
            b={profession:s}
            a.append(b)

    # print(a)


# 写入文件
def write(name):
    fq = open(name+'.txt', 'w+',encoding='utf-8')
    for line in a:
        for index, key in enumerate(line):
            print(key + ' ' + str(line[key]))
            fq.write(key + ' ' + str(line[key]) + '\n')


if __name__ == '__main__':
    x=15
    spider(urls[x])
    write(names[x])
    # for x in range(16):
    #     spider(urls[x])
    #     write(names[x])