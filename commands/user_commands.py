from discord.ext import commands

class UserCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 

    @commands.command(name = "help") 
    async def help(self, ctx):
        pass

async def setup(bot):
    await bot.add_cog(UserCommands(bot))