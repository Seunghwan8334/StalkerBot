from discord.ext import commands

class StalkerGuild():
    def __init__(self):
        self.chat = None
        self.stalkee_list = []

class Stalker(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 
        self.guilds = {}
    
    def add_guild(self, guild_id):
        if guild_id not in self.guilds:
            print("성공적으로 추가 됨")
            self.guilds[guild_id] = StalkerGuild()
    
    def remove_guild(self, guild_id):
        if guild_id in self.guilds:
            del self.guilds[guild_id] 
    
async def setup(bot):
    await bot.add_cog(Stalker(bot))