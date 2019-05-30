#  Lock版本

import threading
import random
import time

gMoney = 1000  # 总的金钱
gLock = threading.Lock()
# 记录生产者生产的次数，达到10次就不再生产
gTimes = 0


class Producer(threading.Thread):  # 生产者
    def run(self):
        global gMoney
        global gLock
        global gTimes
        while True:
            money = random.randint(100, 1000)  # 随机金额
            gLock.acquire()  # 给gMoney加锁
            # 如果已经达到10次了，就不再生产了
            if gTimes >= 10:
                gLock.release()
                break
            gMoney += money
            print('%s当前存入%s元钱，剩余%s元钱' % (threading.current_thread(), money, gMoney))
            gTimes += 1
            time.sleep(0.5)
            gLock.release()


class Consumer(threading.Thread):  # 消费者
    def run(self):
        global gMoney
        global gLock
        global gTimes
        while True:
            money = random.randint(100, 500)
            gLock.acquire()
            if gMoney > money:
                gMoney -= money
                print('%s当前取出%s元钱，剩余%s元钱' % (threading.current_thread(), money, gMoney))
                time.sleep(0.5)
            else:
                # 如果钱不够了，有可能是已经超过了次数，这时候就判断一下
                if gTimes >= 10:
                    gLock.release()
                    break
                print("%s当前想取%s元钱，剩余%s元钱，不足！" % (threading.current_thread(), money, gMoney))  # 得到当前线程名字
            gLock.release()


def main():
    for x in range(5):  # 启动5个线程
        Consumer(name='消费者线程%d' % x).start()

    for x in range(5):
        Producer(name='生产者线程%d' % x).start()


if __name__ == '__main__':
    main()