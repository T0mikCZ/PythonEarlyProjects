import os
import random
import discord
import math
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")
PF = os.getenv("PREFIX")

intents = discord.Intents.all()
bot = commands.Bot(intents=intents, command_prefix=PF)

#ON READY
@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

#COMMANDS
@bot.command()
async def helpic(ctx):
    await ctx.channel.send( "1. helpic\n"
                            "2. pravidlaci\n"
                            "3. soud\n"
                          )

@bot.command()
async def pravidlaci(ctx):
    await ctx.channel.send( "**@everyone\n"
                            "1. Zadne spamovani, hlavne mistr @ADAM\n"
                            "2. Nadavani je povoleno, ale do urcite meze. TAKE KLID\n"
                            "3. Server je hlavne o anime. Vse ostatni pis v #general\n"
                            "4. Rasismus hlavne ne, nebo to lidi nezvladnou\n"
                            "5. NSFW v #nsfw, hmmmm ale ten kanal tady neni lol\n"
                            "6. Zadne propagovani ostatni tvorby bez dotazu**\n"
                          )

@bot.command()
async def soud(ctx, arg):
    if arg in [member.name for member in ctx.guild.members]:
        await ctx.channel.send(f"{arg} jdes k soudu!!!")
    else:
        await ctx.channel.send(f"Jmeno {arg} nenalezeno. Musis zadat jmeno ze serveru.")

@bot.command()
async def role(ctx, arg):
    if not arg or arg == "":
        await ctx.channel.send("Prazdnou roli nemam.")

    role = discord.utils.get(ctx.guild.roles, name=arg)

    if role in ctx.guild.roles and role not in ctx.author.roles:
        try:
            await ctx.author.add_roles(role)
        except commands.errors.CommandInvokeError:
            await ctx.channel.send("Nemas Prava!")
        await ctx.channel.send(f"Role: {arg} pridana.")
    elif role not in ctx.guild.roles:
        await ctx.channel.send(f"Role: {arg} nenalezena.")
    
    else:
        await ctx.channel.send(f"Tuhle roli uz mas!")

@bot.command()
async def mod(ctx):
    modRole = discord.utils.get(ctx.guild.roles, name="Anime Moderátor")
    
    if modRole in ctx.author.roles:
        await ctx.channel.send("Uz jsi moderator")
    else:
        await ctx.author.add_roles(modRole)
        await ctx.channel.send("Uspesne jsi moderator")
bot.run(TOKEN)