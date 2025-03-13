import asyncio
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode
from crawl4ai.content_filter_strategy import PruningContentFilter, BM25ContentFilter
from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator
from crawl4ai import HTTPCrawlerConfig
from crawl4ai.async_crawler_strategy import AsyncHTTPCrawlerStrategy
from crawl4ai.deep_crawling import DeepCrawlStrategy


async def main():
    http_config = HTTPCrawlerConfig(
        method="GET",
        headers={"User-Agent": "MyCustomBot/1.0"},
        follow_redirects=True,
        verify_ssl=True,
    )
    run_config = CrawlerRunConfig(
        cache_mode=CacheMode.DISABLED,
        markdown_generator=DefaultMarkdownGenerator(
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
            url="https://docs.deno.com/runtime/getting_started/installation/",
            config=run_config,
        )
        print((result.markdown.raw_markdown))

        with open("aaaa.txt", "w+") as f:
            f.write(result.markdown.raw_markdown)


if __name__ == "__main__":
    from duckduckgo_search import DDGS

    results = DDGS().text("deno download", max_results=5)
    print(results)
    # asyncio.run(main())
