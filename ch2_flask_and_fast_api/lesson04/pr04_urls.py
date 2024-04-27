import asyncio
import time

import aiohttp
import requests
import threading
import multiprocessing

urls = [
    'https://s01.yapfiles.ru/files/3121945/10.png',
    'https://s01.yapfiles.ru/files/501633/971396276.gif',
    'https://s01.yapfiles.ru/files/11945/1kopiya.jpg'
]


def download(u):
    response = requests.get(u)
    filename = u.split('/')[-1]
    with open('./images/' + filename, 'wb') as file:
        file.write(response.content)
        print(f'Скачан {filename} в папку lesson04')


async def async_download(u):
    async with aiohttp.ClientSession() as session:
        async with session.get(u) as response:
            filename = u.split('/')[-1]
            with open('./images/' + filename, 'wb') as file:
                file.write(await response.read())
                print(f'Скачан {filename} в папку lesson04')


def thread_download():
    start = time.time()
    threads = []
    for url in urls:
        t = threading.Thread(target=download, args=(url,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    print(f'Время выполнения: {time.time() - start}')


def process_download():
    start = time.time()
    processes = []
    for url in urls:
        p = multiprocessing.Process(target=download, args=(url,))
        p.start()
        processes.append(p)
    print(f'Время выполнения: {time.time() - start}')


async def async_await_download():
    start = time.time()
    await asyncio.gather(*[async_download(url) for url in urls])
    print(f'Время выполнения: {time.time() - start}')


if __name__ == '__main__':
    # thread_download()
    # process_download()
    asyncio.run(async_await_download())
