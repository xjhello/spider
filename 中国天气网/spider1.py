from bs4 import BeautifulSoup
import requests
from pyecharts import Bar
ALL_DATA = []

def parse_page(url):
    headers = {
        'User-Agent':
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36 '
    }
    response = requests.get(url, headers=headers)
    text = response.content.decode('utf-8')
    # soup = BeautifulSoup(text, 'lxml')
    soup = BeautifulSoup(text, 'html5lib')  # html5lib解析不规则的HTML代码,速度慢
    conMidtab = soup.find('div', class_='conMidtab')  # 得到div
    tables = conMidtab.find_all('table')
    for table in tables:
        trs = table.find_all('tr')[2:]  # 过滤前两个
        for index, tr in enumerate(trs):
            tds = tr.find_all('td')  # 提取td
            city_td = tds[0]
            if index == 0:
                city_td = tds[1]
            city = list(city_td.stripped_strings)[0]  # 获得城市
            temp_td = tds[-2]
            min_temp = list(temp_td.stripped_strings)[0]  # 最低温度
            ALL_DATA.append({'city': city, 'min_temp': int(min_temp)})
            # print({'city': city, 'min_temp': int(min_temp)})
        # print(table)
    # print(response.content.decode('utf-8'))


def main():
    urls = [
        'http://www.weather.com.cn/textFC/hb.shtml',
        'http://www.weather.com.cn/textFC/db.shtml',
        'http://www.weather.com.cn/textFC/hd.shtml',
        'http://www.weather.com.cn/textFC/hn.shtml',
        'http://www.weather.com.cn/textFC/xb.shtml',
        'http://www.weather.com.cn/textFC/gat.shtml'
    ]
    for url in urls:
        parse_page(url)
    #  分析数据，根据最低气温排序
    ALL_DATA.sort(key=lambda data: data['min_temp'])  # 排序。key是以那个属性排序
    data = ALL_DATA[:10]  # 取前10个
    # print(ALL_DATA)
    # def sorr_key(data):
    #     min_temp = data['min_temp']
    #     return min_temp
    #     pass
    chart = Bar('最低气温柱状图')
    # cities = []
    # temps = []
    cities = list(map(lambda x: x['city'], data))
    temps = list(map(lambda x: x['min_temp'], data))
    chart.add('', cities, temps)
    chart.render('template.html')


if __name__ == '__main__':
    main()
