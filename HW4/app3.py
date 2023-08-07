import os
import sys
import time
import asyncio
import aiohttp


async def download_image(session, url):
    try:
        async with session.get(url) as response:
            if response.status == 200:
                image_name = url.split("/")[-1]
                with open(image_name, "wb") as f:
                    f.write(await response.read())
                print(f"Downloaded {image_name}")
            else:
                print(f"Failed to download {url}")
    except Exception as e:
        print(f"Error while downloading {url}: {e}")


async def main():
    start_time = time.time()

    async with aiohttp.ClientSession() as session:
        tasks = [download_image(session, url) for url in sys.argv[1:]]
        await asyncio.gather(*tasks)

    end_time = time.time()

    total_execution_time = end_time - start_time
    print(f"Total execution time: {total_execution_time:.2f} seconds")


if __name__ == "__main__":
    asyncio.run(main())
