import socket

sk = socket.socket(type=socket.SOCK_DGRAM)
sk.bind(('127.0.0.1', 8989))

while True:
    msg, addr = sk.recvfrom(1024)
    print(addr)
    print(msg.decode('utf-8'))
    info = input('>>>')
    sk.sendto(bytes(info, 'utf-8'), addr)

sk.close()
