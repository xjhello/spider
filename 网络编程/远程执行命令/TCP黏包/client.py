import socket
import subprocess

sk = socket.socket()
sk.connect(('127.0.0.1', 8989))


while True:
    cmd = sk.recv(1024).decode('utf-8')
    ret = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)  # 接受命令并执行，将输出和错误结果给管道

    # 包装信息
    std_out = 'stdout:' + (ret.stdout.read()).decode('gbk')
    std_err = 'stderr:' + (ret.stderr.read()).decode('gbk')
    print(std_out)
    print(std_err)
    sk.send(std_out.encode('utf-8'))  #  返回结果
    sk.send(std_err.encode('utf-8'))

sk.close()