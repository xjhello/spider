import threading

VALUE = 0

gLock = threading.Lock()  # 定义锁


def add_value():
    global VALUE
    gLock.acquire()  # 加锁
    for x in range(1000000):
        VALUE += 1
    gLock.release()   # 解锁
    print('value：%d' % VALUE)


def main():
    for x in range(2):
        t = threading.Thread(target=add_value)
        t.start()


if __name__ == '__main__':
    main()