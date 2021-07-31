import discord
from logger import logger


class DiscordClient(discord.Client):
    def __init__(self, whitelisted_guilds):
        logger.info("Bot Client instance created")
        self.whitelisted_guilds = whitelisted_guilds
        super().__init__()
    
    async def on_ready(self):
        logger.info("%s has been connected", self.user)
        
        for guild in self.guilds:
            if guild.id not in self.whitelisted_guilds:
                await guild.leave()
                logger.warning("Bot has been invited into guild %s, " \
                               "but it was not whitelisted", guild.name)

