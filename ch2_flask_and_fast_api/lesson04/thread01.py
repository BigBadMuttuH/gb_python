import threading
import time


def worker(num):
    print('start thread', num)
    time.sleep(3)
    print('end thread', num)


threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()


print('all threads finished')
