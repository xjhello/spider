from urllib import request

url = 'http://httpbin.org/ip'
# 使用ProxyHandler，传入代理创建handler
handler = request.ProxyHandler({'http':'46.209.135.201:41567'})
# 传入handler创建opener
opener = request.build_opener(handler)
# 使用opener发送请求
resp = opener.open(url)
print(resp)