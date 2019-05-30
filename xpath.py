from urllib import request
from lxml import etree

# 构建解析器
parser = etree.HTMLParser(encoding='utf-8')
# 读取外部文件
html = etree.parse('tencent.html', parser=parser)

# 1.获取所有tr标签
# xpath函数返回的是列表
# trs = html.xpath('//tr')
# for tr in trs:
#     print(etree.tostring(tr, encoding='utf-8').decode('utf-8'))

# 2.获取第二个tr标签,得到的也是列表
# trs = html.xpath('//tr[2]')[0]
# print(etree.tostring(trs, encoding='utf-8').decode('utf-8'))

# 3.获取所有class等于even的tr标签 [@]:获取拥有该属性的标签
# trs = html.xpath("//tr[@class='even']")
# for tr in trs:
#     print(etree.tostring(tr, encoding='utf-8').decode('utf-8'))

# 4.获取所有a标签的href属性的值！
# aList = html.xpath('//a/@href')
# for ab in aList:
#     print(ab)

# <tr class="even">
#  <td class="l square">
# <a target="_blank" href="position_detail.php?id=43730&keywords=&tid=87&lid=0">MIG12-高级服务器开发工程师（深圳）</a></td>
# <td>技术类</td>
# <td>2</td>
# <td>深圳</td>
# <td>2018-08-28</td>
# </tr>

# 5.获取职位信息(纯文本)
# 在某个标签下，再执行xpath函数，获取这个标签下的子孙元素
# 那么应该在//前加一个点，代表是在当前元素下获取
trs = html.xpath('//tr[position()>1]')  # 过滤第一个
# for tr in trs:
#     print(etree.tostring(tr, encoding='utf-8').decode('utf-8'))
#     # print('**************')
#     href = tr.xpath('.//a/@href')[0]
#     title = tr.xpath("./td[1]//text()")[0]
#     category = tr.xpath('./td[2]/text()')[0]
#     nums = tr.xpath('./td[3]/text()')[0]
#     print(href,title)
#     # break

positions = []
for tr in trs:  # 加// 表示获取所有子元素，不加//则获取直接包含的子元素
    href = tr.xpath('.//a/@href')[0]  # 加//也意味着寻找所有HTML中的a标签html.xpath('//a'),要加.
    fullurl = 'https://hr.tencent.com' + href
    title = tr.xpath("./td[1]//text()")[0]  # /是因为td是tr下子元素
    category = tr.xpath('./td[2]/text()')[0]
    nums = tr.xpath('./td[3]/text()')[0]
    address = tr.xpath('./td[4]/text()')[0]
    time = tr.xpath('./td[5]/text()')[0]
    # 组装
    position = {
        'url': fullurl,
        'title': title,
        'category': category,
        'nums': nums,
        'address': address,
        'pubtime': time
    }
    positions.append(position)

print(positions)

