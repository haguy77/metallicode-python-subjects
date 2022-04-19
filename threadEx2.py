import threading
import time

def worker():
    print('hello from thread', repr(threading.current_thread()))
    time.sleep(2)
    print(f'{repr(threading.current_thread())} still working...')
    time.sleep(2)
    print(repr(threading.current_thread()), ' finished')
   
t1 = threading.Thread(target=worker)
t2 = threading.Thread(target=worker)
t1.start()
t1.join(timeout=1.5)
print(f'is_alive before start - {t2.is_alive()}')
t2.start()

#time.sleep(3)
print(f'is_alive after start - {t2.is_alive()}')
# t1.join()
t2.join()
print(f'is_alive after join - {t2.is_alive()}')
print('main exit')