import socket

sk = socket.socket()
sk.bind(('127.0.0.1', 8989))
sk.listen()

conn, addr = sk.accept()
#  黏包本质不知道发送段的长度
ret1 = conn.recv(12)
print(ret1)
ret2 = conn.recv(12)  # 这里会堵塞等待消息，当client段断默认发送空消息就结束
#  优化算法，连续的小数据包被合并
print(ret2)

# print(ret1.decode('utf-8'))
# print(ret2.decode('utf-8'))

conn.close()
sk.close()
