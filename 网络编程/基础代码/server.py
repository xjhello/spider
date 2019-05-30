import socket

sk = socket.socket()
sk.bind(('127.0.0.1', 8898))  # 把地址绑定到套接字
sk.listen()  # 监听链接
conn, addr = sk.accept()  # 接受客户端链接
# print(sk.accept())
while True:
    ret = conn.recv(1024).decode('utf-8')  # 接收客户端信息, 1024为接受个字节
    if ret == 'bye':
        break
    print(ret)  # 打印客户端信息
    enter = input('>>>')
    conn.send(bytes(enter, encoding='utf-8'))  # 向客户端发送信息  必须传入bytes类型,encoding表示说明python字符编码是utf-8，
    # 转化是按照utf-8的标准转化为bytes类型
conn.close()  # 关闭客户端套接字
sk.close()  # 关闭服务器套接字(可选)
