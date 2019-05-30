from urllib import request
url = 'http://dev.kdlapi.com/api/getproxy/?orderid=994591120685989&num=100&b_pcchrome=1&b_pcie=1&b_pcff=1&b_android=1&protocol=1&method=2&an_an=1&an_ha=1&sep=1'

# 请求头
headers = {
    'User-Agent':
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36 '
}
req = request.Request(url)
resp = request.urlopen(req)
print(resp)
# fp = open('data.txt','r')
# ips = []
# for line in fp.readlines():
#     ip = line.strip()
#     ips.append(ip)
#
# print(ips)