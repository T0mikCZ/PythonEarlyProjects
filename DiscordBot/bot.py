import os
import random
import discord
import math
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
LUCIAN_SERVER_ID = os.getenv("LUCIAN_SERVER_ID")
PF = os.getenv("PREFIX")

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    for guild in client.guilds:
        for member in guild.members:
            print(f"{member.name}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.author.name == "Budha":
        await message.channel.send("ONO TO ZIJE POG")
    if message.content == PF + "rozsudek":
        await message.channel.send(f"{message.author.mention} je vinen kokotem")
    if message.content == PF + "popisek luciana":
        if message.author.name == "kunkos152":
            await message.channel.send(f"LUCIANE TY SE ZNAS NEJVIC")
        else:
            await message.channel.send(f"Lucian ma vlasy na kredenc\nVahu ma 80KG\nMa rad hambace")
    if message.content == PF + "popisek adama":
        if message.author.name == "adam je nej voe":
            await message.author.add_roles(discord.utils.get(message.guild.roles, name = "Muted"))
        else:
            await message.channel.send(f"Adam ma vlasy jak kajumY\nVahu ma 10KG\nMa rad tycinky\nVysku ma jak slenderman")
    if message.content == PF + "TRIHARDBOIS":
        await message.channel.send(f"TRASH. CO VIC CHCES RICT")
    if message.content == PF + "petr milf":
        await message.channel.send(f"My name is Petr Milf. I'm 12 years old. My panelák is in the northeast section of Liberec, where all the paneláci are, and I am not married. I work as an employee for the HTML programators , and I get home every day by 8 PM at the latest. I don't smoke, but I occasionally drink. I'm in bed by 1 AM, and make sure I get four hours of sleep, no matter what. After having a glass of warm milk and doing about twenty minutes of HTML stretches before going to bed, I usually have no problems sleeping until morning. Just like a baby, I wake up without any fatigue or stress in the morning. I was told there were no issues at my last check-up. I'm trying to explain that I'm a person who wishes to live a very HTML life. I take care not to trouble myself with any enemies, like winning and losing, that would cause me to lose hentai at night. That is how I deal with society, and I know that is what brings me happiness. Although, if I were to fight I wouldn't lose to anyone.")
    if message.content == PF + "prikaznicy":
        await message.channel.send(f"Zakladni vec je ze musis napsat \"{PF}\" pred jakymkoliv prikaznikem\n1. rozsudek\n2. popisek luciana\n3. popisek adama\n4. TRIHARDBOIS\n5. petr milf\n6. prikaznicy")
    if message.content == PF + "pravidlaci":
        await message.channel.send("@everyone\n 1.Nebudes me srat\n2.Nebudes srat bota zmrde\n3.Zadne zneuzivani bota\n4.Musis mit rad anime kapp")
    if message.content == PF + "depressed lucian":
        await message.channel.send(file=discord.File("C:/Python/DiscordBot/lucian.png"))
    if message.content == PF + "nani":
        await message.channel.send(file=discord.File("C:/Users/Tomyk/Pictures/hnatkova pica.png"))
    if message.content == PF + "kurva padam!":
        await message.channel.send("https://tenor.com/bvpri.gif")
    if message.content == PF + "moje zada":
        await message.channel.send("https://tenor.com/view/spiderman-peter-parker-tobey-maguire-ouch-my-back-gif-14276113")
    if message.content == PF + "stirek":
        await message.channel.send("https://www.europeanpharmaceuticalreview.com/wp-content/uploads/scorpion-750x500.jpg")
    #Rates Part
    if message.content == PF + "urci":
        randomChance = random.randint(0,100)
        await message.channel.send(f"{message.author.mention} je {randomChance}% kokot!")
    if message.content == PF + "pp" or message.content == PF + "penis" or message.content == PF + "penisek" or message.content == PF + "delka":
        randomChance = random.randint(0,25)
        
        if randomChance == 0:
            await message.channel.send(f"{message.author.mention} nema penis XD")
        else:
            penisLenght = "="*randomChance
            await message.channel.send(f"{message.author.mention}' Penisek 8{penisLenght}D")
    if message.content == PF + "iq":
        randomIq = random.randint(55, 250)
        randomIqBalance = random.randint(-35,25)
        randomIqDestroyer = random.randint(0,3)

        finalIq = math.floor(randomIq + randomIqBalance - 5 - (randomIq / 3 + randomIqBalance - 15))

        if randomIq >= 200 and randomIqDestroyer == 1:
            finalIq -= 125
        await message.channel.send(f"{message.author.mention}' IQ is {finalIq}")
    if message.content == PF + "milost?":
        randomChance = random.randint(0,3)
        if randomChance >= 1:
            await message.channel.send(f"NEDOSTANES MILOST!")
        else:
            await message.channel.send(f"Milost pro tebe")
    #JoJo PART
    if message.content == PF + "ORA":
        await message.channel.send("https://tenor.com/view/ora-starplatinum-jojosbizarreadventure-jojo-gif-5505650")
    if message.content == PF + "MUDA":
        await message.channel.send("https://tenor.com/view/muda-theworld-jojosbizarreadventure-%E7%84%A1%E9%A7%84-gif-5455737")
    if message.content == PF + "ARI":
        await message.channel.send("https://tenor.com/view/jojos-bizarre-adventure-jojos-bizarre-adventure-vento-aureo-jojos-bizarre-adventure-golden-wind-bruno-bucciarati-jojo-bruno-gif-18568433")
    if message.content == PF + "DORA":
        await message.channel.send("https://tenor.com/view/jojo-bizzarre-adventure-crazy-diamond-anime-punch-ora-ora-gif-17195212")
    if message.content == PF + "MUDAA":
        await message.channel.send("https://tenor.com/view/ger-muda-gold-experience-requiem-giorno-giovanna-scrundy-pundy-gif-18958486")
    if message.content == PF + "Requiem":
        await message.channel.send("https://tenor.com/view/this-is-requiem-gold-experience-gif-18520329")
    if message.content == PF + "Za Warudo":
        await message.channel.send("https://tenor.com/view/za-warudo-zawarudo-the-world-gif-10578246")
    if message.content == PF + "Secret Technique":
        await message.channel.send("https://tenor.com/view/jojo-run-away-joseph-joestar-jojos-bizarre-adventures-gif-15566885")
    if message.content == PF + "trish" and message.channel.is_nsfw():
        await message.channel.send(file=discord.File("C:/Python/DiscordBot/trishuna.jpg"))
client.run(TOKEN)