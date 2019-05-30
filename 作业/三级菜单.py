#作业一: 三级菜单
#要求:
# 打印省、市、县三级菜单
# 可返回上一级
# 可随时退出程序

menu = {
    '北京':{
        '海淀':{
            '五道口':{
                'soho':{},
                '网易':{},
                'google':{}
            },
            '中关村':{
                '爱奇艺':{},
                '汽车之家':{},
                'youku':{},
            },
            '上地':{
                '百度':{},
            },
        },
        '昌平':{
            '沙河':{
                '老男孩':{},
                '北航':{},
            },
            '天通苑':{},
            '回龙观':{},
        },
        '朝阳':{},
        '东城':{},
    },
    '上海':{
        '闵行':{
            "人民广场":{
                '炸鸡店':{}
            }
        },
        '闸北':{
            '火车战':{
                '携程':{}
            }
        },
        '浦东':{},
    },
    '山东':{},
}


before = []  # 之前的层，可理解为位置指针
now = menu  # 当前的层
while True:
    for i in now:  # 一开始就最外层的列表中
        print(i)
    choice = input('>>>').strip()
    if choice not in now:  # 如果为空跳过后续部分继续要求输入
        continue
    if choice in now:
        before.append(now)  # 以前的层指针前移，相当于复制一个列表
        now = now[choice]  # 指针后移
    elif choice == 'b':  # 退出
        if len(before) != 0:
            now = before.pop()
        else:
            print('到顶了!')
    elif choice == 'q':
        break