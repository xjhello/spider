import socket

sk = socket.socket(type=socket.SOCK_DGRAM)
ip_port = ('127.0.0.1', 8989)  # 发送的地址（元组）

sk.sendto(b'hello!', ip_port)
ret, addr = sk.recvfrom(1024)  # 每次接受的消息要有地址，因为udp是无状态连接
print(ret.decode('utf-8'))


sk.close()