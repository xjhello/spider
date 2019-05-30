import socket
#  UDP 服务器端被动接受消息
sk = socket.socket(type=socket.SOCK_DGRAM)
sk.bind(('127.0.0.1', 8989))

mgs,addr = sk.recvfrom(1024)   # UDP的接受方式，1024指接受的字节
print(mgs.decode('utf-8'))
sk.sendto(b'bb', addr)  # UDP 的发送方式
sk.close()