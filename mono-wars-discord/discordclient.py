import discord
from logger import logger


class DiscordClient(discord.Client):
    def __init__(self, whitelisted_guilds):
        logger.info("Bot Client instance created")
        self.whitelisted_guilds = whitelisted_guilds
        super().__init__()
    
    async def check_guild_or_leave(self, guild: discord.Guild):
        if guild.id not in self.whitelisted_guilds:
            await guild.leave()
            logger.warning("Bot has been invited into guild %s (id: %d), " \
                           "but it was not whitelisted", guild.name, guild.id)
  
    
    async def on_ready(self):
        logger.info("%s has been connected", self.user)
        
        for guild in self.guilds:
            await self.check_guild_or_leave(guild)
    
    async def on_guild_join(self, guild: discord.Guild):
        logger.info("Bot joined the guild %s", guild.name)
        await self.check_guild_or_leave(guild)
