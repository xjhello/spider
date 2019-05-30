'''
在使用requests 时,

* 需要安装 pip install -U 'requests[socks]'

* 提取代理是选择socks5 协议

* 为运行程序的机器添加白名单
'''
import requests
import base64


def base_code(username, password):
    str = '%s:%s' % (username, password)
    encodestr = base64.b64encode(str.encode('utf-8'))
    return '%s' % encodestr.decode() 

url = "https://h.wandouip.com/get/ip-list?pack=0&num=20&xy=1&type=2&lb=\r\n&mr=1&"

ip_port = 'xx.xx.xx.xx:xxxx' # 从api中提取出来的代理IP:PORT
username = '1054746393@qq.com'
password = 'xujian'

basic_pwd = base_code(username, password)

headers = {
    'Proxy-Authorization': 'Basic %s' % (base_code(username, password))
}

proxy = {
    'http': 'socks5://{}'.format(ip_port),
    'https': 'socks5://{}'.format(ip_port)
}

r = requests.get(url,proxies=proxy, headers=headers)
print(r.text)

