import socket

sk = socket.socket(type=socket.SOCK_DGRAM)

ip_port = ('127.0.0.1', 8989)

while True:
    info = input('用户2：')
    info = ('\033[32m来自用户2的消息: %s \033[0m' % info)
    sk.sendto(bytes(info, encoding='utf-8'), ip_port)
    msg,addr = sk.recvfrom(1024)
    print(msg.decode('utf-8'))
sk.close()