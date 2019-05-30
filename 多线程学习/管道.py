from multiprocessing import Pipe,Process


#  在两个进程之间传递数据
def func(conn):
    conn.send('123')


if __name__ == '__main__':
    conn1, conn2 = Pipe()
    Process(target=func,args=(conn1, )).start()
    print(conn2.recv())
