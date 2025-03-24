import threading
counter = 0
lock = threading.Lock()
print(f'{lock.locked()}')

def inc(name):
    global counter
    lock.acquire()
    for i in range(1000):
        counter += 1
        print(f'{name} | {counter} | {lock}')
    lock.release()
    
def dec(name):
    global counter
    lock.acquire()
    for i in range(1000):
        counter -= 1
        print(f'{name} | {counter} | {lock}')
    lock.release()

th1 = threading.Thread(target=inc, args=('th-1-inc',))
th2 = threading.Thread(target=inc, args=('th-2-inc',))
th3 = threading.Thread(target=dec, args=('th-3-dec',))
th4 = threading.Thread(target=dec, args=('th-4-dec',))

for thr in [th1, th2, th3, th4]:
    thr.start()

for thr in [th1, th2, th3, th4]:
    thr.join()
    
print(f'Final counter: {counter}')