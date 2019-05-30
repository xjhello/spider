import time
import random
from urllib import request
import requests
import threading


url = 'http://www.91gxsp.com/share/316690#'
headers = {
    'User-Agent':
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36 '
}
ip_url = ''
i=0
ips = []


class Papa(object):
    global url,handlers

    def go1(self):
        # k=random.randint(0, 100)
        k = 1
        j = 0
        l = 1
        for i in range(0, 200):
            ip_url = ips[k]
            print('第{}个ip：{}'.format(k, ip_url))
            proxies = {
                'http': 'http://{}'.format(ip_url)
            }
            j += 1
            print('第{}次请求'.format(l))
            l += 1
            if j == 2:
                k += 1
                j = 0
                # print('暂停！')
            try:
                print('网络请求.....')
                response = requests.get(url, proxies=proxies, headers=headers,timeout=5)
                time.sleep(0.3)
                print('请求完成.....')
                print(response.status_code)
                if response.status_code == 200:
                    for a in range(0, 3):
                        print('网络请求.....')
                        response = requests.get(url, proxies=proxies, headers=headers, timeout=5)
                        time.sleep(0.3)
                        print('请求完成.....')
                    print('\033[1;31;40成功！\033[0m')
                else:
                    print('\033[1;35m 失败 \033[0m！')
                    print(response.status_code)
            except requests.exceptions.ProxyError :
                print("ip失效跳过！！！！！！！！！！！！！！！！！！！！！！！")
            except requests.exceptions.ConnectionError:
                print("超时跳过！！！！！！！！！！！！！！！！！！！！！！！")
            except requests.exceptions.ReadTimeout:
                print("超时跳过！！！！！！！！！！！！！！！！！！！！！！！")


    def go2(self):
        req = request.Request(url, headers=headers)
        j = 0
        for i in range(0, 200):
            time.sleep(5)
            j += 1
            print(j)
            if j == 4:
                j = 0
                print('暂停5S！')
                time.sleep(10)
            # resp = opener.open(url)
            try:
                print('网络请求.....')
                resp = request.urlopen(req)
                print('请求完成.....')
            except BaseException as e:
                print(e)
                exit(0)


fp = open('data.txt', 'r')
ips = []
for line in fp.readlines():
    ip = line.strip()
    ips.append(ip)
a = Papa()
# a.go2()
a.go1()