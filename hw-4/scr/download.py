import requests
import os
import time
import concurrent.futures
import asyncio
import aiohttp

def download_image(url):
    filename = os.path.basename(url)
    response = requests.get(url)
    if response.status_code == 200:
        with open(os.path.join('hw-4\images', filename), 'wb') as f:
            f.write(response.content)
        return f"Downloaded {filename}"
    else:
        return f"Failed to download {filename}"

def download_images_threaded(urls):
    start_time = time.time()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = executor.map(download_image, urls)
    end_time = time.time()
    for result in results:
        print(result)
    print(f"Total execution time for threaded approach: {end_time - start_time} seconds")

async def download_image_async(session, url):
    filename = os.path.basename(url)
    async with session.get(url) as response:
        if response.status == 200:
            with open(os.path.join('hw-4\images', filename), 'wb') as f:
                f.write(await response.read())
            return f"Downloaded {filename}"
        else:
            return f"Failed to download {filename}"

async def download_images_async(urls):
    start_time = time.time()
    async with aiohttp.ClientSession() as session:
        tasks = [download_image_async(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
    end_time = time.time()
    for result in results:
        print(result)
    print(f"Total execution time for asynchronous approach: {end_time - start_time} seconds")
