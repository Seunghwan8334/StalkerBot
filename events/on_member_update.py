import discord
from discord.ext import commands

class OnMemberUpdate(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.Stalker = bot.get_cog("Stalker")

    @commands.Cog.listener()
    async def on_member_update(self, before: discord.Member, after:discord.Member):
        guild = before.guild
        Stalker = self.Stalker.guilds[guild.id]

        if Stalker.channel is None:
            return
        
        if before.nick != after.nick:
            Stalker.channel





async def setup(bot):
    await bot.add_cog(OnMemberUpdate(bot))