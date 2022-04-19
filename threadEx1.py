import threading
import time

def sleepyWorker():
    
    print('hello from sleepyWorker')
    time.sleep(2)
#     print('hello from sleepyWorker')
   
t1 = threading.Thread(target=sleepyWorker, daemon=True)
t1.start()

#time.sleep(3)

t1.join()
print('main exit')