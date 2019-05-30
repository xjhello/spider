#  服务端，上传下载文件，用户登录

import socket

sk = socket.socket()
sk.bind(('127.0.0.1',8989))
sk.listen()
conn, addr = sk.accept()

while True:
    pass


conn.close()
sk.close()



