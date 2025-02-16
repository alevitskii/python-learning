import time
from threading import Thread
from urllib.request import urlopen


def crawl_one_url(url: str) -> None:
    html = urlopen(url)
    _ = html.read()


def main() -> None:
    urls_to_crawl = [
        "https://www.cnn.com/",
        "https://www.foxnews.com/",
        "https://www.dawn.com",
        "https://www.cnbc.com",
    ]
    start = time.time()

    threads: list[Thread] = []
    for url in urls_to_crawl:
        threads.append(Thread(target=crawl_one_url, args=(url,)))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    elapsed = time.time() - start
    print(f"\n{len(urls_to_crawl)} URLS downloaded in {elapsed:.2f}s")


if __name__ == "__main__":
    main()
