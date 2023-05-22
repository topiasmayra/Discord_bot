<<<<<<< HEAD
import discord
from discord.ext import commands
from imdb import Cinemagoer

intents = discord.Intents.all()
intents.typing = False
intents.presences = False

client = discord.Client(intents=intents)
client = commands.Bot(command_prefix='!', intents=intents)


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(
        type=discord.ActivityType.watching,
        name='Hard Ticket to Hawaii'
    ))
    print('Bot is ready')

# Funtions that moves movie titles to the correct channels
@client.event
async def on_raw_reaction_add(payload):
    if str(payload.emoji) == '<:Segal:1109089566926835753>':
        channel_id = payload.channel_id
        channel = client.get_channel(channel_id)
        message = await channel.fetch_message(payload.message_id)

        if message.author != client.user:
            print(f'Content: {message.content}')
            watchlist_channel_id = 1108863004289798164  # Channel name steve
            watchlist_channel = client.get_channel(watchlist_channel_id)

            if watchlist_channel is None:
                return

            await watchlist_channel.send(message.content)
            await message.delete()
    elif str(payload.emoji) == '<:Donna:1109096237476622336>':
        channel_id = payload.channel_id
        channel = client.get_channel(channel_id)
        message = await channel.fetch_message(payload.message_id)

        if message.author != client.user:
            print(f'Content: {message.content}')
            watchlist_channel_id = 1108805940498665603  # Channel name sidaris
            watchlist_channel = client.get_channel(watchlist_channel_id)

            if watchlist_channel is None:
                return

            await watchlist_channel.send(message.content)
            await message.delete()
    elif str(payload.emoji) == '<:check_mark:1109211912488620062>':
        channel_id = payload.channel_id
        channel = client.get_channel(channel_id)
        message = await channel.fetch_message(payload.message_id)
        watchlist_channel_id = 1108801625419677777  # Channel  watcheted
        watchlist_channel = client.get_channel(watchlist_channel_id)
        await watchlist_channel.send(message.content)
        await message.delete()
        if watchlist_channel is None:
            return

# Help command for the bot, that shows what emojies do what.


client.run('YOUR TOKEN')

