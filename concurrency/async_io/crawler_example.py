import asyncio
import time

import aiohttp


async def crawl_one_url(url: str, session: aiohttp.ClientSession) -> str:
    async with session.get(url) as resp:
        assert resp.status == 200
        return await resp.text()


async def crawl_urls(urls_to_crawl: list[str]) -> list[str]:
    async with aiohttp.ClientSession() as client:
        work_to_do = [crawl_one_url(url, client) for url in urls_to_crawl]
        return await asyncio.gather(*work_to_do)


def main() -> None:
    t0 = time.time()

    urls_to_crawl = [
        "https://www.cnn.com/",
        "https://www.foxnews.com/",
        "https://www.dawn.com",
        "https://www.cnbc.com",
    ]

    asyncio.run(crawl_urls(urls_to_crawl))
    elapsed = time.time() - t0
    print(f"\n{len(urls_to_crawl)} URLS downloaded in {elapsed:.2f}s")


if __name__ == "__main__":
    main()
