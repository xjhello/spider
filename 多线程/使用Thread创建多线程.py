import threading
import time


def coding():
    for x in range(3):
        print('%s正在写代码' % x)
        time.sleep(1)


def drawing():
    for x in range(3):
        print('%s正在画图' % x)
        time.sleep(1)


#  传统模式
def main1():
    coding()
    drawing()


# 多线程
def main2():
    t1 = threading.Thread(target=coding)
    t2 = threading.Thread(target=drawing)
    t1.start()
    t2.start()


if __name__ == '__main__':
    # 传统模式
    #     main1()
    # 多线程
    main2()
