from urllib import request
from urllib import parse
from http.cookiejar import CookieJar

# 创建cookie对象
cookiejar = CookieJar()
# 使用cookejar创建HTTPCookieProcess对象
handler = request.HTTPCookieProcessor(cookiejar)
# 创造opener(请求头)
opener = request.build_opener(handler)
# 使用opener发送登陆请求
headers = {
    'User-Agent':
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36 '
}
data = {
    'email': 15555638392,
    'password': 'xujianzq123'
}
login_url = 'http://www.renren.com/PLogin.do'
req = request.Request(login_url, data=parse.urlencode(data).encode('utf-8'), headers=headers)
opener.open(req)


# 访问主页
zhuye = 'http://www.renren.com/966706284/profile'
# 获取个人主页，使用之前的opener
req = request.Request(zhuye, headers=headers)
resp = opener.open(req)
with open('render.html', 'w', encoding='utf-8') as fp:
    fp.write(resp.read().decode('utf-8'))

