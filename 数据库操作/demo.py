import pymysql

conn = pymysql.connect(
    host="127.0.0.1",
    user='root',
    password='123456',
    database='test',
    port=3306
)
cursor = conn.cursor()

# 插入数据
cursor.execute('input ')
result = cursor.fetchall()
print(result)

conn.commit()
conn.close()