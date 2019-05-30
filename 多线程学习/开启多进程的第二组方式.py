import os
from multiprocessing import Process


class MyProcess(Process):
    def run(self):
        print(self.pid)  # 内部参数
        print(self.name)
        print(os.getpid())


if __name__ == '__main__':
    print('主进程id:', os.getpid())
    p1 = MyProcess()
    p1.start()  #  内部调用run()方法
    p2 = MyProcess()
    p2.start()
    p2.terminate()  #  结束进程

# 自定义类，继承Process
# 必须继承实现run方法，run方法是在子进程中执行的代码
#  结束一个进程不是在执行代码之后立即的结束掉，需要一个操作系统响应的过程
#  检测进程是否活着：is_alive()
