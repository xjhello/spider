import socket

sk = socket.socket()
sk.bind(('127.0.0.1', 8989))
sk.listen()

conn, addr = sk.accept()

while True:
    cmd = input('cmd命令:')
    conn.send(bytes(cmd, 'gbk'))
    num = conn.recv(1024).decode('gbk')  # 先接受要发送的数据长度
    print(num)
    conn.send(b'ok')  # 表示接收到了回应
    res = conn.recv(int(num)).decode('gbk')
    print(res)

conn.close()
sk.close()
