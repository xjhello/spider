import threading
import random
import time

gMoney = 1000
gCondition = threading.Condition()  # 创造类
gTimes = 0
gTotalTimes = 5


class Producer(threading.Thread):
    def run(self):
        global gMoney
        global gCondition
        global gTimes
        while True:
            money = random.randint(100, 1000)
            gCondition.acquire()  # 加锁
            if gTimes >= gTotalTimes:
                gCondition.release()  # 解锁
                print('当前生产者总共生产了%s次' % gTimes)
                break
            gMoney += money
            print('%s当前存入%s元钱，剩余%s元钱' % (threading.current_thread(), money, gMoney))
            gTimes += 1
            time.sleep(0.5)
            gCondition.notify_all()  # 生产完之后通知所有正在等待的线程解锁
            gCondition.release()


class Consumer(threading.Thread):
    def run(self):
        global gMoney
        global gCondition
        while True:
            money = random.randint(100, 500)
            gCondition.acquire()
            # 这里要给个while循环判断，因为等轮到这个线程的时候
            # 条件有可能又不满足了
            while gMoney < money:
                if gTimes >= gTotalTimes:  # 超过次数
                    gCondition.release()
                    return
                print('%s准备取%s元钱，剩余%s元钱，不足！' % (threading.current_thread(), money, gMoney))
                gCondition.wait()  # 钱不够等待状态
            gMoney -= money
            print('%s当前取出%s元钱，剩余%s元钱' % (threading.current_thread(), money, gMoney))
            time.sleep(0.5)
            gCondition.release()


def main():
    for x in range(5):
        Consumer(name='消费者线程%d' % x).start()

    for x in range(2):
        Producer(name='生产者线程%d' % x).start()


if __name__ == '__main__':
    main()
