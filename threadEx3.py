import threading
import time

threadLock = threading.Lock()

def print_time(threadName, delay, counter):
#     threadLock.acquire()
#     while counter:
#         time.sleep(delay)
#         print(f'{threadName},{time.ctime(time.time())}')
#         counter = counter - 1
#     threadLock.release()
    # different syntax (context manager)
    with threadLock:
        while counter:
            time.sleep(delay)
            print(f'{threadName},{time.ctime(time.time())}')
            counter = counter - 1


t1 = threading.Thread(target=print_time, args=(['momo', 2, 3]))
t2 = threading.Thread(target=print_time, args=(['kobi', 1, 3]))
        
t1.start()
t2.start()