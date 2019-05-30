# a={'sda':132,'fff':231}
# # a = ''.join(a)
# for index,key in enumerate(a):
#     # print(a[value])
#     print(index)
#     print(key)
#     print(a[key])
#     # print(a[index])
#
#
# # for x in range(4):
# #     print(x)
import re
number = '213123查夏师傅'
s = re.findall("\D+", number)[0]
print(s)