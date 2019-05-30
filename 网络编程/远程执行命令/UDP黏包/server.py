import socket

sk = socket.socket(type=socket.SOCK_DGRAM)
sk.bind(('127.0.0.1',8989))
mgs, addr = sk.recvfrom(1024)

while True:
    cmd = input('cmd命令:')
    sk.sendto(bytes(cmd.encode('utf-8')), addr)
    mgs, addr = sk.recvfrom(1024)
    print(mgs.decode('utf-8'))

sk.close()


#  UDP 不会黏包，但是会丢包
#  TCP 会黏包，但是不会丢包
