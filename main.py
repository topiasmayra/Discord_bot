import discord
from discord.ext import commands
import asyncio
import os
from dotenv import load_dotenv

import IMDb_search

load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
intents = discord.Intents.all()
intents.typing = False
intents.presences = False
intents.message_content = True
intents.message_content=True
bot = commands.Bot(command_prefix='!', intents=intents,)






@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(
        type=discord.ActivityType.watching,
        name='Hard Ticket to Hawaii'
    ))
    print('Bot is ready')



@bot.event
async def on_raw_reaction_add(payload):
    if str(payload.emoji) == '<:Segal:1109089566926835753>':
        channel_id = payload.channel_id
        channel = bot.get_channel(channel_id)
        message = await channel.fetch_message(payload.message_id)


        print(f'Content: {message.content}')
        watchlist_channel_id = 1108863004289798164  # Channel name steve
        watchlist_channel = bot.get_channel(watchlist_channel_id)

        if watchlist_channel is None:
            return

        await watchlist_channel.send(message.content)
        await message.delete()


    elif str(payload.emoji) == '<:Donna:1109096237476622336>':
        channel_id = payload.channel_id
        channel = bot.get_channel(channel_id)
        message = await channel.fetch_message(payload.message_id)


        print(f'Content: {message.content}')
        watchlist_channel_id = 1108805940498665603  # Channel name sidaris
        watchlist_channel = bot.get_channel(watchlist_channel_id)

        if watchlist_channel is None:
            return

        await watchlist_channel.send(message.content)
        await message.delete()
    elif str(payload.emoji) == '<:check_mark:1109211912488620062>':
        channel_id = payload.channel_id
        channel = bot.get_channel(channel_id)
        message = await channel.fetch_message(payload.message_id)
        watchlist_channel_id = 1108801625419677777  # Channel  watcheted
        watchlist_channel = bot.get_channel(watchlist_channel_id)
        await watchlist_channel.send(message.content)
        await message.delete()
        if watchlist_channel is None:
            return

    elif str(payload.emoji) == '<:kaarme:1130919020644802660>':
        channel_id = payload.channel_id
        channel = bot.get_channel(channel_id)
        message = await channel.fetch_message(payload.message_id)
        await message.delete()




    elif str(payload.emoji) == '<:ehdotus:1111040681666936902>':
        channel_id = payload.channel_id
        channel = bot.get_channel(channel_id)
        message = await channel.fetch_message(payload.message_id)
        watchlist_channel_id = 994331775859949660  # Channel  watcheted
        watchlist_channel = bot.get_channel(watchlist_channel_id)
        await watchlist_channel.send(message.content)
        await message.delete()
        if watchlist_channel is None:
            return




#Bot will message contect of message from DM to the channel.
@bot.event
async def on_message(message):

    if message.author == bot.user:
        return

    if isinstance(message.channel, discord.channel.DMChannel):
        channel = bot.get_channel(994331775859949660)

        if channel:
            await channel.send(f"Vastaanotin yksityisviestin käyttäjältä {message.author}: {message.content}")
        else:
            print("Kanavaa ei löydy!")


# Help command for the bot, that shows what emojies do what.








@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('!etsi'):
        print('Etsi komento käynnistetty')
        await message.channel.send('**Syötä näyttelijän tai ohjaajan nimi!**')

        def check(m):
            return m.author == message.author and m.channel == message.channel

        try:
            user_input = await bot.wait_for('message', check=check, timeout=30)
            personname = user_input.content

            df = IMDb_search.my_search_function(personname)

            if not df.empty:
                await message.channel.send("**Elokuvat:**")
                for title in df['Title']:
                    await message.channel.send(title)
            else:
                await message.channel.send("**En löytynyt elokuvia!**")

        except asyncio.TimeoutError:
                await message.channel.send(f'**Et syöttänyt ohjaajan tai näyttelijän nimeä ylittyi!**')
        except Exception as e:
            await message.channel.send('**Haullasi' + ' ' + personname + 'ei löytynyt mitään.**')
            print('Error occurred:', str(e))

    elif message.content.startswith('!reee'):
        print('Apua komento käynnistetty')


bot.run(DISCORD_TOKEN)
