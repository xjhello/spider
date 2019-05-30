import socket
sk = socket.socket()           # 创建客户套接字
sk.connect(('127.0.0.1', 8898))    # 尝试连接服务器

while True:
    enter = input('>>>')
    sk.send(bytes(enter, encoding='utf-8'))
    ret = sk.recv(1024).decode('utf-8')         # 对话(发送/接收)
    print(ret)
    if ret == 'bye':
        sk.send(b'bye')
        break

sk.close()            # 关闭客户套接字


# send - rev
# send - rev
# rev - send
