import socket
import subprocess

sk = socket.socket(type=socket.SOCK_DGRAM)
ip_port = ('127.0.0.1', 8989)
sk.sendto(b'hi', ip_port)

while True:
    cmd, addr = sk.recvfrom(1024)
    ret = subprocess.Popen(cmd.decode('utf-8'), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)  # 接受命令并执行，将输出和错误结果给管道
    # 包装信息
    std_out = 'stdout:' + (ret.stdout.read()).decode('gbk')
    std_err = 'stderr:' + (ret.stderr.read()).decode('gbk')
    print(std_out)
    print(std_err)
    sk.sendto(std_out.encode('utf-8'), addr)  #  返回结果
    sk.sendto(std_err.encode('utf-8'), addr)

sk.close()