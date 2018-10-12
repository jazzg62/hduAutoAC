from getCode import *
from commitCode import *
import time
import threading

totalProblemN = 6447
thread_lock = threading.BoundedSemaphore(value=3)  # 多线程提交代码

def schedule(pid):
    for i in getCode(pid):
        x = code(pid, 0, i)
        if x.isAccepted():
            print('The problem{} has been AC!'.format(pid))
            break
        else:
            x.submitCode()
            time.sleep(30)
    thread_lock.release()


def main():
    for i in range(1000, totalProblemN + 1):
        # schedule(i)
        thread_lock.acquire()  # 设置线程锁
        T = threading.Thread(target=schedule, args=(i,))
        T.start()


if __name__ == '__main__':
    main()
