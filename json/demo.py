import json

persons = [
    {
        'name': '徐健',
        'age': 18
    },
    {
        'name': 'wang',
        'age': 28
    },
    {
        'name': 'li',
        'age': 38
    }
]

json_str = json.dumps(persons)  # dumps转化成json 序列化
# print(type(json_str))
# print(json_str)
# with open('data.json', 'w', encoding='utf-8') as fp:
#     # fp.write(json_str)
#     json.dump(persons, fp, ensure_ascii=False)   # dump直接将文件输出到文件当中，ascii关闭中文就不会转化成UNcode编码了

# 将json对象转化成python对象（字典）
json_str2 = json.loads(json_str)  # 注意是 loads
print(json_str2)

with open('data.json', 'r', encoding='utf-8') as fp:
    persons = json.load(fp)  # 直接打开json文件
    for person in persons:
        print(person)
