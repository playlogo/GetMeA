import aiohttp
import asyncio

REPO = "SoftFever/OrcaSlicer"


async def check_for_updates():
    async with aiohttp.ClientSession() as session:
        async with session.get(
            f"https://api.github.com/repos/{REPO}/releases"
        ) as response:
            res = await response.json()
            print(res)


if __name__ == "__main__":
    asyncio.run(check_for_updates())
