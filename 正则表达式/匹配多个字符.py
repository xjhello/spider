import re

# 1. * ：匹配0或者任意多个字符:
# text = '02312'
# ret = re.match('\d*', text)  # * 表示匹配多个字符
# print(ret.group())

# 2. + ： 匹配一个或多个字符
# text = 'ab+cd'
# ret = re.match('\w+', text)
# print(ret.group())

# 3. ? ： 匹配一个或者0个
# text = '+1hello'
# ret = re.match('\w?', text)
# print(ret.group())

# 4. {m} 匹配m个字符
# text = 'hello'
# ret = re.match('\w{2}', text)
# print(ret.group())

# 5. {m,n} 匹配m-n个字符
# text = 'abcd'
# ret = re.match('\w{2,5}', text)
# print(ret.group())

# 6. 点. 匹配任意的一个字符 但是不能匹配换行符(\n)
# text = 'hello'
# ret = re.match('.', text)
# print(ret.group())