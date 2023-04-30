import asyncio
import aiohttp
from bs4 import BeautifulSoup as BS
from fake_useragent import UserAgent


BASE_URL = 'https://ru.tradingview.com/markets/cryptocurrencies/prices-all/'
HEADERS = {'User-Agent': UserAgent().random}


async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get(BASE_URL, headers=HEADERS) as response:
            r = await aiohttp.StreamReader.read(response.content)
            soup = BS(r, 'html.parser')

            items = soup.find_all('tr', {"class": 'row-RdUXZpkv listRow'})
            for item in items:
                title = item.find('a', {'class': 'apply-common-tooltip tickerNameBox-GrtoTeat tickerName-GrtoTeat'}).text.strip()
                price = item.find_all('td', {'class': 'cell-RLhfr_y4 right-RLhfr_y4'})[1]




# Супеерррррррррр
                print(title, price.text)



if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())