import discord
from discord.ext import commands


class finder(commands.Cog):
    
    def __inint__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("Initialized finder!")

    @commands.command()
    async def yt(self, ctx, mode, *, querry):
        if mode == "-s":
            result = "https://www.youtube.com/results?search_query="
            if " " in querry:
                querry = querry.replace(" ","+") 
            await ctx.send(result + querry)
        #TODO
        elif mode == "-f":
            await ctx.send(querry)
        await ctx.send("Must provid a valid commend!")

    @commands.command()
    async def phub(self, ctx, *, querry):
        result = "https://www.pornhub.com/video/search?search="
        await ctx.send("Search contains NSFW contents!\n" + result + querry)

    @commands.command()
    async def twt(self, ctx, *, querry):
        result = "https://www.twitch.tv/search?term="
        if " " in querry:
            querry = querry.replace(" ","+")
        await ctx.send(result + querry)

    @commands.command()
    async def web(self, ctx, *, querry):
        result = "https://www.google.com/search?q="
        if " " in querry:
            querry = querry.replace(" ","+")
        await ctx.send(result + querry)

async def setup(client):
    await client.add_cog(finder(client))