#  多进程的组件
import random
import time
from multiprocessing import Process, Semaphore


def ktv(i, sem):
    sem.acquire()  #  获取钥匙
    print('%s走进KTV' % i)
    time.sleep(random.randint(60,180))
    print('%s走出KTV' % i)
    sem.release()  #  换钥匙


if __name__ == '__main__':
    sem = Semaphore(4)   #  信号量，定义多少个锁
    for i in range(20):
        p = Process(target=ktv, args=(i, sem))
        p.start()

