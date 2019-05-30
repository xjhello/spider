import requests

url = 'http://www.baidu.com'

headers = {
    'User-Agent':
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36 '
}
proxies = {
    'http': 'http://31.148.22.110:48745'
}

response = requests.get(url, proxies=proxies, headers=headers)

print(response)

