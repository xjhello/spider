import os
from multiprocessing import Process  # 多进程模块
import time


def func():
    print('12345')
    print('子进程：', os.getpid())
    print('子进程父进程：', os.getppid())


if __name__ == '__main__':
    p = Process(target=func)  #  注册
    # p是一个进程对象，还没有启动
    p.start()  #  启动
    print('父进程：',os.getpid())
    print('父进程的父进程：', os.getppid())