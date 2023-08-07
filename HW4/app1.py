import os
import sys
import time
import threading
import requests


class ImageDownloader(threading.Thread):
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
    threads = []

    for url in sys.argv[1:]:
        thread = ImageDownloader(url)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    end_time = time.time()

    total_execution_time = end_time - start_time
    print(f"Total execution time: {total_execution_time:.2f} seconds")


if __name__ == "__main__":
    main()
    # python app1.py https://otkrit-ka.ru/uploads/posts/2021-10/ochen-smeshnye-foto-kartinki-na-zastavku-1.jpg https://weblinks.ru/wp-content/uploads/2021/08/1-5.jpeg