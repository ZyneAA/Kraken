import asyncio
import os
import discord
from discord.ext import commands


intents = discord.Intents.all()
client = commands.Bot(command_prefix = "$void ",intents = intents)

@client.event
async def on_ready():
    await client.change_presence(status = discord.Status.idle, activity = discord.Game("KO KITT GAY"))
    print("Initialized bot!")

async def load():
    for fname in os.listdir("./cogs"):
        if fname.endswith(".py"):
            await client.load_extension(f"cogs.{fname[:-3]}")

async def main():
    async with client:
        await load()
        await client.start("MTAzMDg5MDU0NzE1NTU4MzA3Ng.G9MLuY.4BfrjG4yxdc1vYURzk9ECUSbquEvD2XvFjAfVg")
asyncio.run(main())
