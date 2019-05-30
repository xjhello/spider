import re

# 1. 匹配某个字符串:
# text = 'hello'
# ret = re.match('he', text)  # match按照'he'规则匹配
# print(ret.group())

# 2. 点. 匹配任意的一个字符 但是不能匹配换行符(\n)
# text = 'hello'
# ret = re.match('.', text)
# print(ret.group())

# 3. \d 匹配任意的数字(0-9)
# text = '1231hello23'
# ret = re.match('\d', text)
# print(ret.group())

# 4. \D 匹配任意的非数字
# text = '@1hello'
# ret = re.match('\D', text)
# print(ret.group())

# 5. \s 匹配空白字符(\n \t \r 空格)  ^\s 非空白
# text = '\n@1hello'
# ret = re.match('\s', text)
# print(ret.group())

# 6. \w 匹配小写a-z 大写A_Z和下划线
# text = '_hello'
# ret = re.match('\w', text)
# print(ret.group())

# 7. \W 与\w相反，匹配非小写a-z 大写A_Z和下划线
# text = '@hello'
# ret = re.match('\W', text)
# print(ret.group())

# 8. []组合的方式，只需要满足括号中的字符，就可以匹配
# text = '0290-2838221'  # \-转义
# ret = re.match('[\d\-]+', text)  # + 意味着一个到多个满足【】中的规则
# print(ret.group())

# 8.1 中括号的形式代替\d
# text = '09'
# ret = re.match('[0-9]', text)
# print(ret.group())

# 8.2 中括号的形式代替\D
# text = 'aa09'
# ret = re.match('[^0-9]', text)  # 加上^ 表示非0-9的字符
# print(ret.group())

# 8.3 中括号的形式代替\w
# text = '09'
# ret = re.match('[a-zA-Z0-9]', text)  #  加上^ 表示非0-9的字符
# print(ret.group())

# 8.4 中括号的形式代替\W
# text = '09'
# ret = re.match('[^a-zA-Z0-9]', text)  #  加上^ 表示非0-9的字符
# print(ret.group())