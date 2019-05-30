import re

# 1. ^（脱字号）：表示以...开始：
# 如果是在中括号中，那么代表的是取反操作.
# text = "hello"
# ret = re.match('^h',text)
# print(ret.group())


# 2. $：表示以...结束：
# 匹配163.com的邮箱
# text = "xxx@163.com"
# ret = re.search('\w+@163\.com$', text)
# print(ret.group())


# 3. |：匹配多个表达式或者字符串：
# text = "http"
# ret = re.match('ftp|http|https', text)
# print(ret.group())


# 4. 贪婪模式和非贪婪模式：
# 非贪婪模式：正则表达式会尽量少的匹配字符。
# 示例代码如下：

# 贪婪模式：正则表达式会匹配尽量多的字符。默认是贪婪模式。
#  例子1
# text = "0123456"
# ret = re.match('\d+', text)  # + 尽量多的字符
# print(ret.group())
#  例子2
# text = "<h1>标题<h1>"
# ret = re.match('<.+?>', text)  # 点. 匹配任意的一个字符, h1>标题<h1 都被点匹配到(+号表示尽可能多的 ?号表示见到第一个>就停止了)
# print(ret.group())


# 可以改成非贪婪模式，那么就只会匹配到0。示例代码如下：
# text = "0123456"
# ret = re.match('\d+?', text)
# print(ret.group())

# 匹配0-100之间数字
text = "99"  # 1,99 100
ret = re.match('[1-9]\d?|100', text)
print(ret.group())