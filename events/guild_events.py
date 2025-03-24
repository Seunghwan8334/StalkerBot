from discord.ext import commands

class GuildEvents(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 
        self.Stalker = bot.get_cog("Stalker")

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        self.Stalker.add_guild(guild.id)
        print(f"봇이 {guild.name} 서버에 들어왔습니다. {guild.id}")

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        self.Stalker.remove_guild(guild.id)
        print(f"봇이 {guild.name} 서버에서 나갔습니다. {guild.id}")


async def setup(bot):
    await bot.add_cog(GuildEvents(bot))