import threading

# def hello():
#     print('hello python')

# print('start')

# t = threading.Timer(3.0, hello)
# t.start()

# print('finish')

ev = threading.Event()

def worker(e):
    while True:
        x = input('enter a char: ')
        if x == 'f':
            e.set()
            break

def worker_2(e):
    while not e.is_set():
        pass
    print('worker_2 says: event is set')
    
t1 = threading.Thread(target=worker, args=(ev,))
t2 = threading.Thread(target=worker_2, args=(ev,))

t1.start()
t2.start()

ev.wait()

print("you entered the letter \'f\'")
quit()