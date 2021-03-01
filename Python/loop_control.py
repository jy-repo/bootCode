
# imports
import threading
import time


# globals
STOP = False


# 현재 thread에서 돌고 있는 process 들의 loop 조건 stop 하여 하던 일 마무리하고 종료
def thread_test():

    global STOP

    th1 = threading.Thread(target=thread_f1, args=())
    th1.start()

    thread_stop_con()

    th1.join()

def thread_stop_con():
    global STOP
    input()
    STOP = True

def thread_f1():

    while not STOP:
        print("thread 1")
        time.sleep(1)