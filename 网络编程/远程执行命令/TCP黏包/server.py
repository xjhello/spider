import socket


sk = socket.socket()
sk.bind(('127.0.0.1', 8989))
sk.listen()

conn, addr = sk.accept()

while True:
    cmd = input('cmd命令:')
    conn.send(bytes(cmd, 'utf-8'))
    rec = conn.recv(1024).decode('utf-8')
    print(rec)

conn.close()
sk.close()
