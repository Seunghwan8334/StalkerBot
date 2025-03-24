from discord.ext import commands

cogs = [
    "commands.admin_commands",

    "cogs.commands",

    "stalker.stalker",
    "stalker.commands",

    "events.message_events",
    "events.guild_events",
    "events.command_errors"
]

async def load_cogs(bot):
    for cog in cogs:
        try:
            await bot.load_extension(cog)
        except Exception as e:
            print(f"{cog}를 로드하는 것을 실패하였습니다. 오류 : {e}")