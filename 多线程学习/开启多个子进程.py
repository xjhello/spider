import time
from multiprocessing import Process


def func(arg1, arg2):
    print('*'*arg1)
    time.sleep(2)
    print('*'*arg2)


if __name__ == '__main__':
    
    p.join()   # 感应一个子进程的结束，将异步程序改为同步
    print('====  运行完毕')