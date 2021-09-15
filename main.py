import discord

client = discord.Client()


@client.event
async def on_ready():
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)
    print("------")


@client.event
async def on_message(message):
    cmd = message.content.split(" ")[0]
    args = message.content.split(" ")[1:]

    if message.content.startswith("!ping"):
        await message.channel.send("pong")


client.run("token")
