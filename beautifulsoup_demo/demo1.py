from bs4 import BeautifulSoup

html = """
 <table class="tablelist" cellpadding="0" cellspacing="0">
		    	<tr class="h">
		    		<td class="l" width="374">职位名称</td>
		    		<td>职位类别</td>
		    		<td>人数</td>
		    		<td>地点</td>
		    		<td>发布时间</td>
		    	</tr>
		    			    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=43730&keywords=&tid=87&lid=0">MIG12-高级服务器开发工程师（深圳）</a></td>
					<td>技术类</td>
					<td>2</td>
					<td>深圳</td>
					<td>2018-08-28</td>
		    	</tr>
		    			    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=43725&keywords=&tid=87&lid=0">MIG12-高级后台开发工程师（深圳）</a></td>
					<td>技术类</td>
					<td>1</td>
					<td>深圳</td>
					<td>2018-08-28</td>
		    	</tr>
		    			    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=43720&keywords=&tid=87&lid=0">25924-手游SDK终端开发高级工程师(深圳)</a></td>
					<td>技术类</td>
					<td>1</td>
					<td>深圳</td>
					<td>2018-08-28</td>
		    	</tr>
		    			    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=43709&keywords=&tid=87&lid=0">24491-资深大数据工程师（深圳）</a></td>
					<td>技术类</td>
					<td>1</td>
					<td>深圳</td>
					<td>2018-08-28</td>
		    	</tr>
		    			    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=43707&keywords=&tid=87&lid=0">SNG11-资深技术工程师（深圳）</a><span class="hot">&nbsp;</span></td>
					<td>技术类</td>
					<td>3</td>
					<td>深圳</td>
					<td>2018-08-28</td>
		    	</tr>
		    			    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=43693&keywords=&tid=87&lid=0">TEG04-腾讯乐享Web前端开发（深圳）</a></td>
					<td>技术类</td>
					<td>2</td>
					<td>深圳</td>
					<td>2018-08-28</td>
		    	</tr>
		    			    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=43678&keywords=&tid=87&lid=0">TEG02-FPGA研发工程师（上海）</a></td>
					<td>技术类</td>
					<td>3</td>
					<td>上海</td>
					<td>2018-08-28</td>
		    	</tr>
		    			    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=43674&keywords=&tid=87&lid=0">23674-新闻后台开发高级工程师（北京）</a></td>
					<td>技术类</td>
					<td>2</td>
					<td>北京</td>
					<td>2018-08-28</td>
		    	</tr>
		    			    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=43667&keywords=&tid=87&lid=0">TEG15-Mysql数据库架构师（深圳）</a></td>
					<td>技术类</td>
					<td>1</td>
					<td>深圳</td>
					<td>2018-08-28</td>
		    	</tr>
		    			    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=43638&keywords=&tid=87&lid=0">25923-弹性计算研发工程师（深圳）</a><span class="hot">&nbsp;</span></td>
					<td>技术类</td>
					<td>1</td>
					<td>深圳</td>
					<td>2018-08-28</td>
		    	</tr>
		    </table>
"""
# bs = BeautifulSoup(html, 'lxml')   # lxml指定解析器
# print(bs.prettify())

soup = BeautifulSoup(html, 'lxml')
# 1. 获取所有tr标签
# trs = soup.find_all('tr')
# for tr in trs:
#     print(tr)

# 2.获取第二个tr标签,得到的也是列表
# trs = soup.find_all('tr', limit=2)[1]  # limit指定获取多少个元素,返回的是列表
# print(trs)

# 3.获取所有class等于even的tr标签
# 方式：
# trs = soup.find_all('tr', class_='even')
# for tr in trs:
#     print(tr)
# # 方式2：
# trs = soup.find_all('tr', attrs='even')  # attribute简写


# 4.获取所有id等于even的tr标签
trs = soup.find_all('tr', id='test', class_='test')
trs = soup.find_all('tr', attrs={'id': 'test', 'class': 'test'})

# 5.获取所有a标签的href属性的值！
# aList = soup.find_all('a')
# for a in aList:
#     # 1. 通过下表操作方式
#     href = a['href']
#     # 2.通过attrs属性的方式
#     href = a.attrs('href')

# 6. 获取所有的职位信息
trs = soup.find_all('tr')[1:]  # 获得所有tr 标签，得到的是列表
positions = []
for tr in trs:
    # 方法1：
    # position = {}
    # tds = tr.find_all('td')  # 获取tr下的td
    # title = tds[0].string     # 第一个td
    # category = tds[1].string
    # num = tds[3].string
    # position['title'] = title
    # position['category'] = category
    # position['num'] = num
    # positions.append(position)
    # 方法2：
    infos1 = list(tr.strings)  # strings提取非标签的字符串全都提取出来，获取子孙非标签字符串
    infos = list(tr.stripped_strings)  # 提取非空白的字符
    print(infos1)
    print(infos)
# print(positions)
