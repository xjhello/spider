import re
from pyecharts import Bar

names = [
    '人文与传播学院',
    '外国语学院',
    '教育学院',
    '音乐学院',
    '谢晋影视艺术学院',
    '商学院',
    '美术学院',
    '数理学院',
    '生命与环境科学学院',
    '旅游学院',
    '体育学院',
    '信息与机电工程学院',
    '哲学与法政学院',
    '对外汉语学院',
    '马克思主义学院',
    '教育硕士管理中心（筹）'
]




a = {}  # 报考人数
b = {}  # 录取人数
pro = []
num = []
name = '报考人数.txt'
fp1 = open(name, 'r',encoding='utf-8')
# fp2 = open('外国语学院.txt','r',encoding='utf-8')
for line in fp1:
    key,value = line.split()
    value = int(value)
    a[key]=value

# for line in fp2:
#     key,value = line.split()
#     value = int(value)
#     b[key]=value



def pi(name):
    fp2 = open(name+'.txt', 'r', encoding='utf-8')
    for line in fp2:
        key, value = line.split()
        value = int(value)
        b[key] = value


for i in names:
    pi(i)



n=0
for index1,key1 in enumerate(b):
    for index2,key2 in enumerate(a):
        if key1 == key2:
            print('报考人数:'+str(a[key2]))
            print('录取人数:' + str(b[key1]))
            fla = (b[key1]/a[key2])
            fla = '%.2f' % fla
            print('专业:'+key1+'  录取率:'+ str(fla))
            name = key1
            s = re.findall("\D", name)[0]
            print(s)
            pro.append(key1)
            num.append(fla)
            n+=1
            print(n)

chart = Bar('上海师范外国语学院录取图')


axisLabel = {
    'interval': 0,
    'rotate': 40
}


chart.add('', pro, num,is_more_utils=True,axisLabel=axisLabel)
chart.render('template.html')
print(pro)
print(num)