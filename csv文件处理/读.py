import csv

# with open('taobao.csv', 'r') as fp:
#     # reader是一个迭代器
#     reader = csv.reader(fp)
#     next(reader)  # 挪指针
#     for x in reader:
#         name = x[0]
#         price = x[6]
#         print(name, price)

with open('taobao.csv', 'r') as fp:
    # DictReader不会包含标题那行的数据，返回的是字典
    reader = csv.DictReader(fp)
    for x in reader:
        print(x)