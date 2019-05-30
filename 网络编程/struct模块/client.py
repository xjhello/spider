#  黏包本质就是不知道要接受多大的数据
import socket
import subprocess
import struct

sk = socket.socket()
sk.connect(('127.0.0.1', 8989))


while True:
    cmd = sk.recv(1024).decode('gbk')
    print(cmd)
    ret = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)  # 接受命令并执行，将输出和错误结果给管道
    # 管道里的数据只能读一次
    # 包装信息
    std_out = ret.stdout.read()
    std_err = ret.stderr.read()
    lenth = len(std_out) + len(std_err)
    num_byte = struct.pack('i', lenth)  # 打包
    sk.send(num_byte)  # 发送固定的4个字节的数据大小
    sk.send(std_out)  # 返回结果
    sk.send(std_err)

sk.close()

#  好处： 确定要接受的数据大小
#  坏处： 多了一次传输
