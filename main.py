import discord
import random
from discord.ext import commands

bot = commands.Bot(command_prefix='/', intents=discord.Intents.all())
phrases = ["Insert your custom phrase here"] # Replace this with your initial phrase(s)

@bot.command(name='insult')
async def generate_phrase(ctx):
    phrase = phrases[random.randint(0, len(phrases)-1)] # Pick a random phrase from the list
    random_member = random.choice(ctx.guild.members) # Pick a random member from the server
    await ctx.send(f"{random_member.mention}, {phrase}") # Mention the random member and send the phrase

@bot.command(name='padd')
async def add_phrase(ctx, *, phrase):
    phrases.append(phrase)
    await ctx.send(f'"{phrase}" has been added to the list of custom phrases.')

@bot.command(name='premove')
async def remove_phrase(ctx, *, phrase):
    try:
        phrases.remove(phrase)
        await ctx.send(f'"{phrase}" has been removed from the list of custom phrases.')
    except ValueError:
        await ctx.send(f'"{phrase}" is not in the list of custom phrases.')

@bot.command(name='plist')
async def list_phrases(ctx):
    phrase_list = "\n".join([f"{index+1}. {phrase}" for index, phrase in enumerate(phrases)])
    await ctx.send(f'List of custom phrases:\n{phrase_list}')


bot.run('') # Replace this with your bot token
