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

soup = BeautifulSoup(html, 'lxml')

# css选择器
# 1. 获取所有tr标签
# trs = soup.select('tr')
# for tr in trs:
#     print(tr)


# 2.获取第二个tr标签,得到的也是列表
# trs = soup.select('tr')[1]
# print(trs)


# 3.获取所有class等于even的tr标签
# trs = soup.select('tr.even')
# trs = soup.select('tr[class=even]')
# for tr in trs:
#     print(tr)


# 4.获取所有a标签的href属性的值！
# aList = soup.select('a')
# for a in aList:
#     href = a['href']
#     print(href)


# 5.获取所有文本
# trs = soup.select('tr')
# for tr in trs:
#     infos = list(tr.stripped_strings)
#     print(infos)