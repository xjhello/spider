import requests
from lxml import etree

# 1. 将目标网站页面抓取
headers = {
    'User-Agent':
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36 ',
    'Referer':
        'https://movie.douban.com/'
}

url = 'https://movie.douban.com/cinema/nowplaying/shanghai/'
response = requests.get(url, headers=headers)
text = response.text
# print(response.text)
# response.text，返回的是一个经过解码后的字符串，是str（Unicode）类型
# response.content返回的是原生的字符串，从网页上抓取下来的，没有经过处理的字符串，是bytes类型

#  2.将抓取下来的数据根据一定规则提取
html = etree.HTML(text)
# 得到的是一个列表
ul = html.xpath("//ul[@class='lists']")[0]
lis = ul.xpath("./li")
movies = []
for li in lis:
    title = li.xpath("@data-title")[0]
    score = li.xpath("@data-score")[0]
    duration = li.xpath("@data-duration")[0]
    region = li.xpath("@data-region")[0]
    director = li.xpath("@data-director ")[0]
    actors = li.xpath("@data-actors ")[0]
    thumbnail = li.xpath(".//img/@src")[0]

    movie = {
       'title ': title,
       'score': score,
       'duration': duration,
       'region': region,
       'director': director,
       'actors': actors,
       'thumbnail': thumbnail,
    }
    movies.append(movie)

for iteam in movies:
    print(iteam)

# <li id="26636712" class="list-item" data-title="蚁人2：黄蜂女现身" data-score="7.5" data-star="40" data-release="2018" data-duration="119分钟(中国大陆)" data-region="美国" data-director="佩顿·里德" data-actors="保罗·路德 / 伊万杰琳·莉莉 / 迈克尔·佩纳" data-category="nowplaying" data-enough="True" data-showed="True" data-votecount="87989" data-subject="26636712">
#                         <ul class="">
#                             <li class="poster">
#                                 <a href="https://movie.douban.com/subject/26636712/?from=playing_poster" class="ticket-btn" target="_blank" data-psource="poster">
#                                     <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2529389608.webp" alt="蚁人2：黄蜂女现身" rel="nofollow" class="">
#                                 </a>
#                             </li>
#                             <li class="stitle">
#                                 <a href="https://movie.douban.com/subject/26636712/?from=playing_poster" class="ticket-btn" target="_blank" title="蚁人2：黄蜂女现身" data-psource="title">
#                                     蚁人2：黄蜂女...
#                                 </a>
#                             </li>
#                             <li class="srating">
#                                         <span class="rating-star allstar40"></span>
#                                         <span class="subject-rate">7.5</span>
#                             </li>
#                                 <li class="sbtn">
#                                     <a class="ticket-btn" href="https://movie.douban.com/ticket/redirect/?url=https%3A%2F%2Fm.maoyan.com%2Fcinema%2Fmovie%2F343208%3F_v_%3Dyes%26merCode%3D1000011" target="_blank">
#                                         选座购票
#                                     </a>
#                                 </li>
#                         </ul>
#                     </li>
