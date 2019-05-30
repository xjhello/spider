import struct

ret = struct.pack('i', 2049)  # i代表int,就是即将要把一个数字转化成固定长度的bytes类型
print(ret)

num = struct.unpack('i', ret)  # 解包 返回的是个元组
print(num)

# 发送数据的时候，先发送长度，先接受数据的长度
