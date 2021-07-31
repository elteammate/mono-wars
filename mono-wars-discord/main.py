import os
import asyncio
import dotenv

from app import app
from discordclient import DiscordClient


async def main():
    dotenv.load_dotenv()
    try:
        await run_web_server()
        await run_discord_client()
    except KeyboardInterrupt:
        await app.stop_async()


async def run_web_server():
    await app.run_async(int(os.getenv("SERVER_PORT")))


async def run_discord_client() -> DiscordClient:
    token = os.getenv("DISCORD_TOKEN")
    whitelisted_guilds_string = os.getenv("WHITELISTED_GUILDS")
    whitelisted_guilds = list(map(int, whitelisted_guilds_string.split(',')))
    client = DiscordClient(whitelisted_guilds)
    app.discord = client
    await client.start(token)
 

if __name__ == "__main__":
    asyncio.run(main())
