from bot_logic import *
import discord

emojes()
games()
gen_pass(10)

# Переменная intents - хранит привилегии бота
intents = discord.Intents.default()
# Включаем привелегию на чтение сообщений
intents.message_content = True
# Создаем бота в переменной client и передаем все привелегии
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$ILY'):
        await message.channel.send("I Love You Too :sparkles:")
    elif message.content.startswith('$game'):
        await message.channel.send(games())
    elif message.content.startswith('$emojes'):
        await message.channel.send(emojes())
    elif message.content.startswith('$pass'):
        await message.channel.send(gen_pass(10))
    else:
        await message.channel.send(message.content)

client.run("MTIwMTA2Nzk3MTA0MTMwNDU5OA.G5Ztyb.bcv_5NiEVUg-EpbtDOsVtWG4qxwTYEhBOkyRbA")