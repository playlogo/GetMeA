# Note: Using simple http requests instead of playwright due to massive installation size

import asyncio

from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, CacheMode
from crawl4ai.content_filter_strategy import BM25ContentFilter
from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator
from crawl4ai import HTTPCrawlerConfig
from crawl4ai.async_crawler_strategy import AsyncHTTPCrawlerStrategy


async def async_main(url: str):
    http_config = HTTPCrawlerConfig(
        method="GET",
        headers={"User-Agent": "MyCustomBot/1.0"},
        follow_redirects=True,
        verify_ssl=True,
    )
    run_config = CrawlerRunConfig(
        cache_mode=CacheMode.DISABLED,
        markdown_generator=DefaultMarkdownGenerator(
            # Query doesn't have effect at all...
            content_filter=BM25ContentFilter(user_query="linux", bm25_threshold=100),
        ),
        only_text=True,
        remove_forms=True,
        ignore_body_visibility=False,
        exclude_external_images=True,
        exclude_external_links=True,
        exclude_social_media_links=True,
    )

    async with AsyncWebCrawler(
        crawler_strategy=AsyncHTTPCrawlerStrategy(browser_config=http_config)
    ) as crawler:
        result = await crawler.arun(
            url=url,
            config=run_config,
        )
        return result.markdown.raw_markdown


def main(url: str):
    res = asyncio.run(async_main(url))

    return res
