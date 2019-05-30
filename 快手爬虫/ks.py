import requests
import re
import urllib.request
from bs4 import BeautifulSoup

# 伪装浏览器
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36'
        }

urls = []
j = 1


def get_url():
    fp = open('ks2000.txt', 'r')
    i = 0
    for line in fp.readlines():
        i += 1
        url = line.strip()
        urls.append(url)
        if(i>30):
            break


def down():
    global j
    for u in urls:
        # html = requests.get(u, headers=headers)
        if j <= 20:
            try:
                print('正在下载第{}个视频'.format(j))
                urllib.request.urlretrieve(u, 'G:\\video\{}.mp4'.format(j))
                print('下载完成')
                j += 1
            except urllib.error.HTTPError:
                print('下载失败！')
        else:
            break


def main():
    get_url()
    # for i in urls:
    #     print(i)
    down()


if __name__ == '__main__':
    main()







# # 定义一个下载函数
# def dowload(url):
#     # 梨视频世界杯栏目地址
#     # url = 'http://www.pearvideo.com/category_9'
#     # 使用beautifulsoup剖析网页的工具
#     html = requests.get(url, headers=headers)
#     soup = BeautifulSoup(html.text, 'html.parser')
#     for video in soup.select('.vervideo-bd'):
#         # 获取视频的id
#         id = video.select('a')[0]['href']
#         # 获取标题
#         title = video.select('.vervideo-title')[0].text
#         # 根据观察分析出视频页面的地址
#         new_url = 'http://www.pearvideo.com/{}'.format(id)
#         # 获取视频页面的地址后剖析出真正播放的视频地址
#         res = requests.get(new_url, headers=headers, timeout=3).text
#         # 利用正则表达式获取
#         req = re.compile(r'srcUrl="(.*?)"')
#         url_getVideo = re.findall(req, res)[0]
#         global i
#         print('正在下载第{}个视频'.format(i), title, url_getVideo)
#         # 保存视频
#         urllib.request.urlretrieve(url_getVideo, 'E:\\unity\image\{}.mp4'.format(i))
#         i += 1
#
#
# # 动态页面的获取函数
# def dowloadmore():
#     n = 12
#     while True:
#         if n > 36:
#             return
#         ##http://www.pearvideo.com/category_loading.jsp?reqType=5&categoryId=9&start=24&mrd=0.8168488163466117&hotContIds=1375878,1375886,1375856
#         # http://www.pearvideo.com/category_loading.jsp?reqType=5&categoryId=9&start=36&mrd=0.5650126657752985&hotContIds=1375878,1375886,1375856
#         # 通过chrome浏览器分析，获取动态页面的地址，发现地址后面是12的倍数
#         url = 'http://www.pearvideo.com/category_loading.jsp?reqType=5&categoryId=9&start={}'.format(n)
#         n += 12
#         dowload(url)
#
#
# i = 1
# dowloadmore()












