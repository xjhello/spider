import time
from urllib import request
import urllib
import os

url = 'http://www.91gxsp.com/share/316690#'
api_url = 'https://h.wandouip.com/get/ip-list?pack=0&num=20&xy=1&type=2&lb=\r\n&mr=1&'
ips = []


class papa():
    url = 'http://www.91gxsp.com/share/316690#'
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36 '
    }
    handler = request.ProxyHandler({'http': '47.94.230.42:9999'})

    def go1(self):
        # 传入handler创建opener
        opener = request.build_opener(handler)
        # 使用opener发送请求
        # resp = opener.open(url)
        j = 0
        for i in range(0, 200):
            time.sleep(1)
            j += 1
            print(j)
            if j == 4:
                j = 0
                print('暂停5S！')
                time.sleep(10)
            resp = opener.open(url)
            print(resp)

    def go2(self):
        req = request.Request(url, headers=headers)
        j = 0
        for i in range(0, 200):
            time.sleep(1)
            j += 1
            print(j)
            if j == 4:
                j = 0
                print('暂停5S！')
                time.sleep(10)
            # resp = opener.open(url)
            resp = request.urlopen(req)


def api():
    fp = open('data.txt', 'r')
    for line in fp.readlines():
        ip = line.strip()
        ips.append(ip)

handler = request.ProxyHandler({'http': '117.90.137.102:3617'})
# 请求头
headers = {
    'User-Agent':
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36 '
}

# opener = request.build_opener(handler)
# resp = opener.open(url)
req = request.Request(url, headers=headers)
# resp = request.urlopen(req)
j=0
for i in range(0,200):
    time.sleep(1)
    j+=1
    print(j)
    if j==4:
        j=0
        print('暂停5S！')
        time.sleep(10)
    # resp = opener.open(url)
    try:
        print('网络请求.....')
        resp = request.urlopen(req)
        print('请求完成.....')
    except urllib.error.HTTPError:
        print('太快了！')
        os.system("5.py")

# a = list(range(0,4))
# print(a)