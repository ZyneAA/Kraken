import discord
from discord.ext import commands


class purge(commands.Cog):
    
    def __inint__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("Initialized purge!")

    @commands.command()
    async def rm(self, ctx, amount = 0):
        await ctx.channel.purge(limit = amount + 1)

async def setup(client):
    await client.add_cog(purge(client))



