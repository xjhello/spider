import time
from multiprocessing import Process


def func():
    time.sleep(0.5)
    print('我还活着')


if __name__ == '__main__':
    p = Process(target=func)
    p.daemon = True    #  设置子进程为守护进程
    p.start()
    i = 0
    while i < 10:
        print('我是socket ')
        time.sleep(1)
        i += 1

#  守护进程会随着主进程代码的结束而结束