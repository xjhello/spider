# 分组：
# 在正则表达式中，可以对过滤到的字符串进行分组。分组使用圆括号的方式。
#     group：和group(0)是等价的，返回的是整个满足条件的字符串。
#     groups：返回的是里面的子组。索引从1开始。
#     group(1)：返回的是第一个子组，可以传入多个。
#     示例代码如下：
import re
# text = "apple price is $99,orange price is $10"
# ret = re.search(r".*(\$\d+).*(\$\d+)",text)
# print(ret.group())  # 匹配整个字符串
# print(ret.group(0))  # 匹配整个字符串
# print(ret.group(1))
# print(ret.group(2))
# print(ret.groups())


# findall：
# 找出所有满足条件的，返回的是一个列表。
# text = 'apple price $99 orange price $88'
# ret = re.findall('\d+', text)
# print(ret)


# sub：
# 用来替换字符串。将匹配到的字符串替换为其他字符串。
# text = 'apple price $99 orange price $88'
# ret = re.sub('\d+', '0', text)
# print(ret)

# sub函数的案例，获取拉勾网中的数据：
html = """
<div>
<p>基本要求：</p>
<p>1、精通HTML5、CSS3、 JavaScript等Web前端开发技术，对html5页面适配充分了解，熟悉不同浏览器间的差异，熟练写出兼容各种浏览器的代码；</p>
<p>2、熟悉运用常见JS开发框架，如JQuery、vue、angular，能快速高效实现各种交互效果；</p>
<p>3、熟悉编写能够自动适应HTML5界面，能让网页格式自动适应各款各大小的手机；</p>
<p>4、利用HTML5相关技术开发移动平台、PC终端的前端页面，实现HTML5模板化；</p>
<p>5、熟悉手机端和PC端web实现的差异，有移动平台web前端开发经验，了解移动互联网产品和行业，有在Android,iOS等平台下HTML5+CSS+JavaScript（或移动JS框架）开发经验者优先考虑；6、良好的沟通能力和团队协作精神，对移动互联网行业有浓厚兴趣，有较强的研究能力和学习能力；</p>
<p>7、能够承担公司前端培训工作，对公司各业务线的前端（HTML5\CSS3）工作进行支撑和指导。</p>
<p><br></p>
<p>岗位职责：</p>
<p>1、利用html5及相关技术开发移动平台、微信、APP等前端页面，各类交互的实现；</p>
<p>2、持续的优化前端体验和页面响应速度，并保证兼容性和执行效率；</p>
<p>3、根据产品需求，分析并给出最优的页面前端结构解决方案；</p>
<p>4、协助后台及客户端开发人员完成功能开发和调试；</p>
<p>5、移动端主流浏览器的适配、移动端界面自适应研发。</p>
</div>
"""
# ret = re.sub('<.+?>',"",html)  # 贪婪模式
# # ret = re.sub('</?[a-zA-Z0-9]+>',"",html)
# print(ret)

# split使用正则表达式来分割字符串。
text = "hello world ni hao"
ret = re.split('\W',text) # 以空格分割
print(ret)


# compile：
# 对于一些经常要用到的正则表达式，可以使用compile进行编译，后期再使用的时候可以直接拿过来用，
# 执行效率会更快。而且compile还可以指定flag=re.VERBOSE，在写正则表达式的时候可以做好注释。示例代码如下：

text = "the number is 20.50"  # 规则合集！！！！！！
r = re.compile('\d+\.?\d*')
# r = re.compile(r"""
#                 \d+ # 小数点前面的数字
#                 \.? # 小数点
#                 \d* # 小数点后面的数字
#                 """, re.VERBOSE)      # re.VERBOSE表示可以换行写 和注释
ret = re.search(r,text)
print(ret.group())
