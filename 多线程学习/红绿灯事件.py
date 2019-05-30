# 红绿灯事件
import time
import random
from multiprocessing import Event, Process


def cars(e, i):
    if not e.is_set():
        print('car%i在等待' % i)
        e.wait()  # 阻塞 直到得到一个 事件状态变成 True 的信号
    print('\033[0;32;40mcar%i通过\033[0m' % i)


def light(e):
    while True:
        if e.is_set():
            e.clear()  # 改变状态
            print('\033[31m红灯亮了\033[0m')
        else:
            e.set()   # 改变状态
            print('\033[32m绿灯亮了\033[0m')
        time.sleep(2)


if __name__ == '__main__':
    e = Event()
    traffic = Process(target=light, args=(e,))
    traffic.start()
    for i in range(20):
        car = Process(target=cars, args=(e, i))
        car.start()
        time.sleep(random.random())
