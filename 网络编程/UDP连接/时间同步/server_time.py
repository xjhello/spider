import socket
import time

sk = socket.socket(type=socket.SOCK_DGRAM)
sk.bind(('127.0.0.1', 8989))

msg, addr = sk.recvfrom(1024)
now_time = time.strftime("%Y-%m-%d %X")
if msg.decode('utf-8') == 'now':
    sk.sendto(bytes(now_time, 'utf-8'), addr)


