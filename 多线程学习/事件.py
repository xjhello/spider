# 通过一个信号 来控制 多个进程 同时 执行或者阻塞
# 事件
# 一个信号可以使所有的进程都进入阻塞状态
# 也可以控制所有的进程解除阻塞
# 一个事件被创建之后,默认是阻塞状态
from multiprocessing import Event

e = Event()  # 创建了一个事件
print(e.is_set())   # 查看一个事件的状态,默认被设置成阻塞
e.set()      # 将这个事件的状态改为True
print(e.is_set())
e.wait()     # 是依据e.is_set()的值来决定是否阻塞的
print(123456)
e.clear()    # 将这个事件的状态改为False
print(e.is_set())
e.wait()     # 等待 事件的信号被变成True
print('*'*10)

# set 和 clear
#      分别用来修改一个事件的状态 True或者False
# is_set 用来查看一个事件的状态
# wait 是依据事件的状态来决定自己是否在wait处阻塞
#      False阻塞 True不阻塞


