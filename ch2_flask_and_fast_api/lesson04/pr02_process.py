import os
import time
import multiprocessing
from pathlib import Path


def process_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        contents = f.read()
        count = len(contents.split())
        print(f'{file_name}: {count} words')


if __name__ == '__main__':
    start = time.time()
    dir_path = Path('../')
    file_paths = os.walk(dir_path, )

    processes = []
    for root, dirs, files in file_paths:
        files = [os.path.join(root, file) for file in files if file.endswith('.py')]
        for file in files:
            t = multiprocessing.Process(target=process_file, args=(file, ))
            processes.append(t)
            t.start()

    for t in processes:
        t.join()

    print(f'Total time: {time.time() - start:.2f} seconds')
