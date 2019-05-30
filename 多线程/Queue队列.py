import threading
import time
from queue import Queue


# 创建队列
# q = Queue(4)

def set_value(q):
    index = 0
    while True:
        q.put(index)  # 数据放入到队列当中
        index += 1
        time.sleep(2)


def get_value(q):
    while True:
        print(q.get())  # 队列没有数就堵塞等待


if __name__ == '__main__':
    q = Queue(4)
    t1 = threading.Thread(target=set_value, args=[q])
    t2 = threading.Thread(target=get_value, args=[q])
    t1.start()
    t2.start()

# Queue(maxsize)：#创建一个先进先出的队列。
# qsize()#返回队列的大小。
# empty()#判断队列是否为空。
# full()#判断队列是否满了。
# get()#从队列中取最后一个数据。
# put()#将一个数据放到队列中。
