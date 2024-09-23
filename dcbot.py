import discord
import bot_mantik
import wowoa

# ayricaliklar (intents) değişkeni botun ayrıcalıklarını depolayacak
intents = discord.Intents.default()
# Mesajları okuma ayrıcalığını etkinleştirelim
intents.message_content = True
# client (istemci) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaralım
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yaptık.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$merhaba'):
        await message.channel.send("Selam!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\U0001f642")
    elif message.content.startswith("$sa"):
        await message.channel.send("as")
    elif message.content.startswith("$nasılsın"):
        await message.channel.send("iyiyim sen nasılsın")
    elif message.content.startswith("$iyi"):
        await message.channel.send("ne güzel")
    elif message.content.startswith("$şifre"):
        await message.channel.send(wowoa.gen_pass(10))
    elif message.content.startswith("$para"):
        await message.channel.send(bot_mantik.yazi_tura())
    elif message.content.startswith("$emo"):
        await message.channel.send(bot_mantik.emoji_olusturucu())
    else:
        await message.channel.send(message.content)

client.run("0000")
