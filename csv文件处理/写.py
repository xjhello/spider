import csv

# 1.
header = ['name', 'age', 'demo']
value = [
    ('张三', 12, 11),
    ('李四', 23, 12)
]
# with open('data.csv', 'w', encoding='utf-8', newline='') as fp:
#     writer = csv.writer(fp)
#     writer.writerow(header)
#     writer.writerow(value)

# 2.字典方式写入
# with open('data.csv', 'w', encoding='utf-8', newline='') as fp:
#     writer = csv.DictReader(fp, header)
#     writer.writeheader()
