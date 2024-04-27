import os
import time
import asyncio
from pathlib import Path


async def process_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        contents = f.read()
        count = len(contents.split())
        print(f'{file_name}: {count} words')


async def main():
    tasks = []
    dir_path = Path('../')
    file_paths = os.walk(dir_path, )

    for root, dirs, files in file_paths:
        files = [os.path.join(root, file) for file in files if file.endswith('.py')]
        for file in files:
            task = asyncio.create_task(process_file(file))
            tasks.append(task)

    await asyncio.gather(*tasks)

if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    print(f'Total time: {time.time() - start:.2f} seconds')
