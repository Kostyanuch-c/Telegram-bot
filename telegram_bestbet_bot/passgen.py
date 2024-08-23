from typing import Optional, Dict, Any
import time
import asyncio
import aiohttp
from dotenv import load_dotenv
import os

class Bot:
    def __init__(self, bot_token: str):
        self.API_URL = f"https://api.telegram.org/bot{bot_token}"
        self.stdout_notify = "Был апдейт"
        self.offset = -1

    def do_something(self) -> None:
        print(self.stdout_notify)

    async def get_updates(
            self, session: aiohttp.ClientSession
    ) -> Optional[Dict[str, Any]]:
        api_url = f"{self.API_URL}/getUpdates?offset={self.offset}"
        try:
            async with session.get(api_url) as response:
                response.raise_for_status()
                return await response.json()
        except (aiohttp.ClientError, asyncio.TimeoutError):
            return

    async def run(self) -> None:
        while True:
            start_time = time.time()

            async with aiohttp.ClientSession() as session:
                updates = await self.get_updates(session)
                if updates and updates.get("result"):
                    for result in updates['result']:
                        self.offset = result['update_id'] + 1
                        self.do_something()
            await asyncio.sleep(3)
            end_time = time.time()
            print(f'Время между запросами к Telegram Bot API: {end_time - start_time}')


if __name__ == "__main__":
    load_dotenv()
    TOKEN = os.getenv('BOT_TOKEN')
    BOT = Bot(TOKEN)
    asyncio.run(BOT.run())