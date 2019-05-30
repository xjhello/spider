import socket

sk = socket.socket()

sk.connect(('127.0.0.1', 8989))

while True:
    info = input('>>>')
    sk.send(info.encode('utf-8'))
    res = sk.recv(1024)
    print(res.decode('utf-8'))
sk.close()