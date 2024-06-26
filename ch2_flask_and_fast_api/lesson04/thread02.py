import threading
import time

counter = 0


def increment():
    global counter
    for _ in range(1_000_000):
        counter += 1
    print(f'counter = {counter:_}')


threads = []
for i in range(5):
    t = threading.Thread(target=increment)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(f'counter final = {counter:_}')
