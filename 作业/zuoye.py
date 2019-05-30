# 1.统计元组中所有数据属于字符串的个数，提示：isinstance()
# 数据：t1 = (1, 2, '3', '4', 5, '6')
# 结果：3
t1 = (1, 2, '3', '4', 5, '6')
count = 0
for i in t1:
    if isinstance(i, str):  # 此处有坑？
        count +=1
print(count)


# 2.将以下数据存储为字典类型
# 数据：info = "name:Owen|age:18|gender:男"
# 结果：{'name': 'Owen', 'age': 18, 'gender': '男'}
info = "name:Owen|age:18|gender:男"
infos = info.split('|')  # 切割存储到列表中
info_dic = {}
for msg in infos:
    k, v = msg.split(':')  # 再次切割，打散存储
    if v.isdigit():  # 数字字符串强制类型转化为int类型
        v = int(v)
    info_dic[k] = v  # 字典赋值
print(info_dic)


# 3.完成数据的去重
# 数据：t3 = (1, 2, 1, 2, 3, 5, 9)
# 结果：t3 = (1, 2, 3, 5, 9)
# 注：从不考虑顺序、考虑顺序两方面完成
# 方法1:
t3 = (1, 2, 1, 2, 3, 5, 9)  # tuple类型，不可改变的
l3 = []
for v in t3:
    if v not in l3:
        l3.append(v)  # 列表添加
t3 = tuple(l3)  # 列表转化为元组
print(t3)
# 方法2:
t3 = (1, 2, 1, 2, 3, 5, 9)
t3 = tuple(set(t3))  # set集合，不出现相同的数据
print(t3)


# 4.计算元组中所有可以转换为数字的数据的总和
# 数据：t4 = (10, 'abc', '100', '3')
# 运算结果：113
t4 = (10, 'abc', '100', '3')
total = 0
for v in t4:
    if isinstance(v, int):  # int为指定判断类型，这里判断是否为int
        total += v
    elif isinstance(v, str):
        if v.isdigit():
            v = int(v)
            total += v
print(total)


# 5.将数据转换类型存储
# 原数据：dic = {'name': 'Owen', 'age': 18, 'gender': '男'}
# 处理后：info = [('name', 'Owen'), ('age', 18), ('gender', '男')]
# 方法1：
dic = {'name': 'Owen', 'age': 18, 'gender': '男'}
info = []
for k, v in dic.items():  # 以列表返回可遍历的(键, 值) 元组数组
    info.append((k, v))
print(info)
# 方法2：
dic = {'name': 'Owen', 'age': 18, 'gender': '男'}
info = []
for index, key in enumerate(dic):  # 使用枚举，index为下标，可以为字典的键
    info.append((key, dic[key]))
print(info)


# 拓展1.计算元组中所有可以转换为数字的数据的总和
# 数据：t4 = (10, 'abc', '100', '3', '壹', '肆', [1000], (10000,))
# 运算结果：11118
# 提示：
#   -- 利用字符串isnumeric()判断汉字
# 	-- 利用字典{'壹': 1 ...}将汉字转换为数字
#	-- 利用isinstance()将list和tuple中数据取出来
#	-- 先将所有转化为数字的数据存放在一个单列集合中，在做运算

# 方法1：
t4 = (10, 'abc', '100', '3', '壹', '肆', [1000], (10000,))
#  中文数字对应表
num_map = {'壹': 1, '贰': 2, '仨': 3,
           '肆': 4, '伍': 5, '陆': 6,
           '柒': 7, '捌': 8, '玖': 9, '拾': 10}
nums = []
for v in t4:
    if isinstance(v, int):  # 判断是否为int
        nums.append(v)
    elif isinstance(v, str):
        if v.isdigit():
            nums.append(int(v))
        elif v.isnumeric():  # isnumeric()可以判断中文数字
            nums.append(num_map[v])
    elif isinstance(v, tuple) or isinstance(v, list):  # 判断是否为其他数据类型
        # 只考虑该具体数据，不考虑更复杂情况
        for n in v:
            nums.append(n)
total = sum(nums)  # python内置方法
print(total)

# 方法2：
t4 = (10, 'abc', '100', '3', '壹', '肆', [1000], (10000,))
#  中文数字对应表
num_map = {'壹': 1, '贰': 2, '仨': 3,
           '肆': 4, '伍': 5, '陆': 6,
           '柒': 7, '捌': 8, '玖': 9, '拾': 10}
num = 0  # 总和初始化
for i in t4:
    if isinstance(i,int):
        num += i
    elif isinstance(i,str):
        if i.isdigit():
            num += int(i)
        elif i.isnumeric():
            num += num_map[i]
    elif isinstance(i, tuple) or isinstance(i, list):  # 处理其他列表和元组里面的数据，和前面的一样再遍历一次就好了
        for j in i:
            if isinstance(j, int):
                num += j
            elif isinstance(j, str):
                if j.isdigit():
                    num += int(j)
                elif j.isnumeric():
                    num += num_map[j]
print(num)


# 拓展2.完成录入电话本
# 需求：
'''
-- 从键盘中录入姓名(不区分大小写)：
	-- 姓名必须是全英文组成，不是则重新录入姓名，如果是q，代表退出
-- 从键盘中再录入电话：
	-- 电话必须为数字且长度必须是11位(不能转换为数字)
-- 如果出现姓名相同，则保留最后一次电话号码
-- 形成的数据是有电话分组的，如：第一次录入Owen，13355667788，则会形成
	-- {
    	'O': {
    		'Owen': '13355667788'
    	}
	}

最终数据，分组名一定大写：
{
    'E': {
		'egon': '17788990000',
		'engo': '16633445566'
    },
    'O': {
    	'Owen': '13355667788'
    }
}
'''

# 电话本
phone_map = {}
# 是否退出系统
is_over = False
while not is_over:
    # 姓名初始制空，完成只有姓名输入正确才录入电话
    name = ''
    while True:
        # 姓名必须录入正确
        if not name:
            name = input("name：")
            if name == 'q':
                # 退出系统
                is_over = True
                break
            elif not name.isalpha():  # 全为英文
                # 录入错误，置空名字
                print('name error')
                name = ''
                continue
        # 录入电话，保证是11位的数字字符串
        phone = input("phone：")
        if not (phone.isdigit() and len(phone) == 11):
            continue

        # 取组名
        group = name[0:1].upper()
        # 对于组名的操作：无组名，添加分组 | 有组名，不操作
        phone_map.setdefault(group, {})
        phone_map[group][name] = phone
        # 一条信息添加完毕，重置信息
        name = ''
        phone = ''
        print('录入成功')
print(phone_map)




