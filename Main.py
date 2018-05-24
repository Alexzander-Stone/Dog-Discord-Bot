import discord
from discord.ext import commands
import asyncio
import time

Client = discord.Client()
client = commands.Bot(command_prefix = "?")

@client.event
async def on_ready():
    print("Bot is ready!")

@client.event
async def on_message(message):
    # upper lets us ignore case sensitivity
    # if message.content.upper().startswith('!SCHEDULE'):
        # userID = message.author.id

    if message.content.upper().startswith('!SCHEDULE'):
        userID = message.author.id
        # <...> helps solve issue with string concatenation with user ids
        await client.send_message(message.channel, "<@%s> Don't worry bruh, I gotchu." % userID)
        # Create array with message contents separated by spaces.
        args = message.content.split(" ")
        await client.send_message(message.channel, "%s" % " ".join(args[1:]))

client.run("Mzc5MDc2MjE2Nzc2NTU2NTU0.Degvvw.7YDZxyKz9BzJhKgkpFfZ0NyXFRg")