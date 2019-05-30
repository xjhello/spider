import socket
import time


sk = socket.socket()
sk.connect(('127.0.0.1', 8989))

sk.send(b'hello!')


time.sleep(5)
sk.close()

#  短时间多个send 小的数据连在一起，可能会发生黏包现象，是tcp协议内部优化算法引起的
