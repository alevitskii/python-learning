import time
from multiprocessing import Process
from urllib.request import urlopen


def crawl_one_url(url: str) -> None:
    html = urlopen(url)
    _ = html.read()


def main() -> None:
    urls_to_crawl = [
        "https://www.cnn.com",
        "https://www.foxnews.com",
        "https://www.dawn.com",
        "https://www.cnbc.com",
    ]

    start = time.time()

    processes: list[Process] = []
    for url in urls_to_crawl:
        processes.append(Process(target=crawl_one_url, args=(url,)))

    for process in processes:
        process.start()

    for process in processes:
        process.join()

    elapsed = time.time() - start
    print(f"\n{len(urls_to_crawl)} URLS downloaded in {elapsed:.2f}s")


if __name__ == "__main__":
    main()
