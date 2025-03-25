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
        
        if before.id in Stalker.stalkee_list: 
            
            if before.nick != after.nick: #닉네임 변경 감지
                if before.nick is None:
                    await Stalker.channel.send(f"{before.mention} 닉네임 변경됨: {before.display_name} -> {after.nick}")
                elif after.nick is None:
                    await Stalker.channel.send(f"{before.mention} 닉네임 변경됨: {before.nick} -> {after.display_name}")
                else:
                    await Stalker.channel.send(f"{before.mention} 닉네임 변경됨: {before.nick} -> {after.nick}")
                return 
            
            if before.name != after.name: #이름 변경 감지
                await Stalker.channel.send(f"{before.mention} 이름 변경됨: {before.name} -> {after.name}")
                return
            
            if before.avatar != after.avatar: #아바타 변경 감지
                await Stalker.channel.send(f"{before.mention} 아바타 변경됨: {before.avatar} -> {after.avatar}")
                return 

            if before.roles != after.roles: #역할 변경 감지
                added_roles = [role for role in after.roles if role not in before.roles]
                removed_roles = [role for role in before.roles if role not in after.roles]

                if added_roles:
                    Stalker.channel.send(f"추가된 역할: {[role.name for role in added_roles]}")
                    
                if removed_roles:
                    Stalker.channel.send(f"제거된 역할: {[role.name for role in removed_roles]}")

            if before.status != after.status: #상태 변경 감지
                await Stalker.channel.send(f"{before.mention} 상태 변경됨: {before.status} -> {after.status}")
                return

            if before.activity != after.activity: #활동 변경 감지
                await Stalker.channel.send(f"{before.mention} 활동 변경됨: {before.activity} -> {after.activity}")
                return


async def setup(bot):
    await bot.add_cog(OnMemberUpdate(bot))