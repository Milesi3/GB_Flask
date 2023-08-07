import os
import sys
import time
import multiprocessing
import requests


class ImageDownloader(multiprocessing.Process):
    def __init__(self, url):
        super().__init__()
        self.url = url

    def run(self):
        try:
            response = requests.get(self.url)
            if response.status_code == 200:
                image_name = self.url.split("/")[-1]
                with open(image_name, "wb") as f:
                    f.write(response.content)
                print(f"Downloaded {image_name}")
            else:
                print(f"Failed to download {self.url}")
        except Exception as e:
            print(f"Error while downloading {self.url}: {e}")


def main():
    start_time = time.time()
    processes = []

    for url in sys.argv[1:]:
        process = ImageDownloader(url)
        process.start()
        processes.append(process)

    for process in processes:
        process.join()

    end_time = time.time()

    total_execution_time = end_time - start_time
    print(f"Total execution time: {total_execution_time:.2f} seconds")


if __name__ == "__main__":
    main()
