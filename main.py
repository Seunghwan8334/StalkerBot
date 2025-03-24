import discord
from discord.ext import commands
from cogs.load_cogs import load_cogs

import os 
from dotenv import load_dotenv 
load_dotenv() 

TOKEN = os.getenv("DISCORD_BOT_TOKEN") 

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
intents.members = True
intents.guilds = True 

bot = commands.Bot(command_prefix='$', intents=intents)
bot.help_command = None

@bot.event
async def on_ready():
    print(f"Logged on as {bot.user}!")

    Stalker = bot.get_cog("Stalker")

    print(f"현재 이 봇은 {len(bot.guilds)}개의 길드에 가입되어 있습니다.")
    for guild in bot.guilds:
        Stalker.add_guild(guild.id)

    print("Bot ready to use!")

@bot.event
async def setup_hook():
    await load_cogs(bot)
    await bot.tree.sync()

if __name__ == "__main__":
    bot.run(TOKEN)