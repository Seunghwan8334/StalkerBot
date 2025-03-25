from discord.ext import commands

class StalkerCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 
        self.Stalker = self.bot.get_cog("Stalker")

    @commands.command(name="set_channel") 
    @commands.has_permissions(administrator=True)
    async def set_channel(self, ctx, channel_mention:str):
        Stalker = self.Stalker.guilds[ctx.guild.id] 
        
        channel_id = int(channel_mention[2:-1])
        channel = ctx.guild.get_channel(channel_id)
        if channel:
            Stalker.channel = channel
            await ctx.send(f"{channel.mention}으로 설정하였습니다.")
        else:
            await ctx.send("해당 채널을 찾을 수 없습니다.")


    @commands.command(name="add_stalkee")
    @commands.has_permissions(administrator=True)
    async def add_stalkee(self, ctx, member_mention:str):
        Stalker = self.Stalker.guilds[ctx.guild.id]
        if Stalker.channel is None:
            await ctx.send("채팅창을 먼저 설정해주세요. \n 명령어: $set_channel 채널맨션")
            return
        
        member_id = int(member_mention[2:-1])
        if member_id in Stalker.stalkee_list:
            await ctx.send("해당 유저는 이미 리스트에 존재합니다.")
            return
        try:
            Stalker.stalkee_list.append(member_id)
            await ctx.send(f"{member_id}를 성공적으로 추가하였습니다.")
        except:
            await ctx.send(f"{member_id}를 추가하는 것을 실패하였습니다.")

    
    @commands.command(name="remove_stalkee")
    @commands.has_permissions(administrator=True)
    async def remove_stalkee(self, ctx, member_mention:str):
        Stalker = self.Stalker.guilds[ctx.guild.id]
        if Stalker.channel is None:
            await ctx.send("채팅창을 먼저 설정해주세요. \n 명령어: $set_channel 채널맨션")
            return

        member_id = int(member_mention[2:-1])
        if member_id not in Stalker.stalkee_list:
            await ctx.send("해당 유저는 리스트에 존재하지 않습니다.")

        try:
            Stalker.stalkee_list.remove(member_id)
            await ctx.send(f"{member_id}를 성공적으로 제거하였습니다.")
        except:
            await ctx.send(f"{member_id}를 제거하는 것을 실패하였습니다.")

    @commands.command(name="stalkee_list")
    @commands.has_permissions(administrator=True)
    async def stalkee_list(self, ctx):
        Stalker = self.Stalker.guilds[ctx.guild.id]
        if Stalker.channel is None:
            await ctx.send("채팅창을 먼저 설정해주세요. \n 명령어: $set_channel 채널맨션")
            return

        message = f"총 {len(Stalker.stalkee_list)} 명의 이름이 있습니다.\n"

        for stalkee in Stalker.stalkee_list:
            message += f"<@{stalkee}>\n"
        message += "끝."

        await ctx.send(message)

async def setup(bot):
    await bot.add_cog(StalkerCommands(bot))