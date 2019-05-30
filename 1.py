import time
import requests

url = 'http://www.91gxsp.com/share/316690#'
api_url = 'https://h.wandouip.com/get/ip-list?pack=0&num=20&xy=1&type=2&lb=\r\n&mr=1&'


proxies = {
    'http': '124.41.193.183:52150'
}

HEADERS = {
    'User-Agent':
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36 ',
    'Referer':
        'https://movie.douban.com/'
}
response = requests.get(url, proxies=proxies, headers=HEADERS)
# 查看响应码
print(response.status_code)

# opener = request.build_opener(handler)
# resp = opener.open(url)
# req = request.Request(url, headers=headers)
# resp = request.urlopen(req)
# j=0
# for i in range(0,600):
#     time.sleep(0.1)
#     j+=1
#     print(j)
#     # resp = opener.open(url)
#     resp = request.urlopen(req)



# print(resp.read().decode('utf-8'))
# with open('1.html', 'w') as fp:
#     fp.write(resp.read().decode('utf-8'))

