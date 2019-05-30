import socket
import struct

sk = socket.socket()
sk.bind(('127.0.0.1', 8989))
sk.listen()

conn, addr = sk.accept()

while True:
    cmd = input('cmd命令:')
    conn.send(bytes(cmd, 'gbk'))
    num = conn.recv(4)  # 先接受固定4字节的bytes。得到了要接受数据的长度
    num = struct.unpack('i',num)[0]  # 解bytes
    print(num)
    res = conn.recv(num).decode('gbk')
    print(res)

conn.close()
sk.close()
