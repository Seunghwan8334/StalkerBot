from discord.ext import commands

class CommandErrors(commands.Cog):

    def __init__(self, bot):
        self.bot = bot 

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("권한이 부족합니다.") 
        elif isinstance(error, commands.CommandNotFound):
            await ctx.send("이런 명령어는 없는데. 오타라도 내셨나요?")
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("명령어 뒤에 (args)을 추가해 주세요")
        elif isinstance(error, commands.MemberNotFound):
            await ctx.send("해당 유저는 존재하지 않습니다.")
        elif isinstance(error, commands.NotOwner):
            await ctx.send("해당 명령어는 봇 소유자만 사용 가능합니다.")
        elif isinstance(error, commands.ChannelNotFound):
            await ctx.send("해당 채널은 존재하지 않습니다.")
        elif isinstance(error, commands.BotMissingPermissions):
            await ctx.send("봇의 권한이 부족합니다.")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("잘못된 입력값입니다.")
        else:
            await ctx.send(f"으잉? 이런 명령어 오류는 예상 못 했는데.. 봇 소유자에게 문의해보세요.")

async def setup(bot):
    await bot.add_cog(CommandErrors(bot))