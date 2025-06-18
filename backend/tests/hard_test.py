import aiohttp
import asyncio
import time

URL = "http://0.0.0.0:8000/buyers/"
TOTAL_REQUESTS = 10000
CONCURRENT_REQUESTS = 10000


async def send_request(session):
    try:
        async with session.get(URL) as response:
            if response.status == 200:
                return True
            else:
                print(f"Ошибка: {response.status}")
                return False
    except Exception as e:
        print(f"Исключение: {e}")
        return False


async def run_test():
    start_time = time.time()

    connector = aiohttp.TCPConnector(limit_per_host=CONCURRENT_REQUESTS)
    async with aiohttp.ClientSession(connector=connector) as session:
        tasks = [send_request(session) for _ in range(TOTAL_REQUESTS)]
        results = await asyncio.gather(*tasks)

        successful = sum(results)
        failed = TOTAL_REQUESTS - successful
        duration = time.time() - start_time

        print(f"\nТест завершен за {duration:.2f} секунд")
        print(f"Успешные запросы: {successful}")
        print(f"Неудачные запросы: {failed}")
        print(f"RPS (запросов в секунду): {TOTAL_REQUESTS / duration:.2f}")


if __name__ == "__main__":
    asyncio.run(run_test())
