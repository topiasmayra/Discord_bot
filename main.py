import discord
from discord.ext import commands
import subprocess
import os
from dotenv import load_dotenv



load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
intents = discord.Intents.all()
intents.typing = False
intents.presences = False
intents.message_content = True
intents.message_content=True

bot = commands.Bot(command_prefix='!' , intents=intents)




@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(
        type=discord.ActivityType.watching,
        name='Hard Ticket to Hawaii'
    ))
    print('Bot is ready')

#Emoji reaction message for the bot, that deletes the message and sends it to the watchlist channel.
@bot.event
async def on_raw_reaction_add(payload):
    if str(payload.emoji) == '<:Segal:1109089566926835753>':
        channel_id = payload.channel_id
        channel = bot.get_channel(channel_id)
        message = await channel.fetch_message(payload.message_id)


    elif str(payload.emoji) == '<:Donna:1109096237476622336>':
        channel_id = payload.channel_id
        channel = bot.get_channel(channel_id)
        message = await channel.fetch_message(payload.message_id)

        if message.author != bot.user:
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

    elif str(payload.emoji) == '<a:DonaBlow:1111037449221705788>':
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
        channel_id = 994331775859949660 #Channel name ehdotukset
        channel = bot.get_channel(channel_id)
        await channel.send(message.content)


# Help command for the bot, that shows what emojies do what.




import IMDb_search

@bot.command()
async def etsi(ctx):
    await ctx.send('**Syötä näyttelijän tai ohjaajan nimi!**')

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    try:
        user_input = await bot.wait_for('message', check=check, timeout=30)
        personname = user_input.content

        df = IMDb_search.my_search_function(personname)

        if not df.empty:
            await ctx.send("**Elokuvat:**")
            for title in df['Title']:
                await ctx.send(title)
        else:
            await ctx.send("**En löytynyt elokuvia!**")

    except TimeoutError:
        await ctx.send('**Et syöttänyt ohjaajan tai näyttelijän nimeä, aikaraja ylittyi!**')
    except Exception as e:
        await ctx.send('**Haullasi' + ' ' + personname + 'ei löytynyt mitään.**')
        print('Error occurred:', str(e))

bot.run(DISCORD_TOKEN)
