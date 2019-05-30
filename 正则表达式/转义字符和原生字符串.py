import re
# 在正则表达式中，有些字符是有特殊意义的字符。因此如果想要匹配这些字符，
# 那么就必须使用反斜杠进行转义。比如$代表的是以...结尾，如果想要匹配$，那么就必须使用\$。示例代码如下：

#  1.
text = "apple price is \$99,orange paice is $88"
ret = re.search('\$(\d+)',text)
print(ret.group())

# 原生字符串：python有两种方式 '\\n', r'\n'
# 在正则表达式中，\是专门用来做转义的。在Python中\也是用来做转义的。因此如果想要在普通的字符串中匹配出\，那么要给出四个\。示例代码如下：
text = "apple \c"
ret = re.search('\\\\c', text)  # 3个\\\
print(ret.group())

# 因此要使用原生字符串就可以解决这个问题：
text = "apple \c"
ret = re.search(r'\\c', text)
print(ret.group())
