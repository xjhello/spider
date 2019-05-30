import re

# 验证手机号码：手机号码的规则是以1开头，第二位可以是34587，后面那9位就可以随意了。示例代码如下：
# text = "18570631587"
# ret = re.match('1[34587]\d{9}', text)
# print(ret.group())

# 而如果是个不满足条件的手机号码。那么就匹配不到了。示例代码如下：
# text = "1857063158"
# ret = re.match('1[34587]\d{9}', text)
# print(ret.group())

# 验证邮箱：邮箱的规则是邮箱名称是用数字、数字、下划线组成的，然后是 @ 符号，后面就是域名了。示例代码如下：
# text = "hynever@163.com"
# 方式1
# ret = re.match('\w+@[a-z0-9]+\.[a-z]+', text)
# 方式2
# ret = re.match('\w+@\w+\.[a-zA-Z\.]+', text)  # \. 转义 表示点
# print(ret.group())

# 验证URL：URL的规则是前面是http或者https或者是ftp然后再加上一个冒号，再加上一个斜杠，再后面就是可以出现任意非空白字符了。示例代码如下：
# text = "http://www.baidu.com/"
# ret = re.match('(http|https|ftp)://[^\s]+', text) # [^\s]+任意多个非空白字符
# print(ret.group())

# 验证身份证：身份证的规则是，总共有18位，前面17位都是数字，后面一位可以是数字，也可以是小写的x，也可以是大写的X。示例代码如下：
# text = "3113111890812323X"
# ret = re.match('\d{17}[\dxX]', text)
# print(ret.group())
