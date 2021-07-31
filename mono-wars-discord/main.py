import os
import dotenv

from discordclient import DiscordClient


def main():
    dotenv.load_dotenv()
    token = os.getenv("DISCORD_TOKEN")
    whitelisted_guilds_string = os.getenv("WHITELISTED_GUILDS")
    whitelisted_guilds = list(whitelisted_guilds_string)
    client = DiscordClient(whitelisted_guilds)
    client.run(token)


if __name__ == "__main__":
    main()
