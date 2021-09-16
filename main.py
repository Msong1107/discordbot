import discord
import requests


client = discord.Client()

data = []
instance_type = [
    ["t2.nano", 1, 0.5],
    ["t2.micro", 1, 1],
    ["t2.small", 1, 2],
    ["t2.medium", 2, 4],
    ["t2.large", 2, 8],
    ["t3.nano", 2, 0.5],
    ["t3.micro", 2, 1],
    ["t3.small", 2, 2],
    ["t3.medium", 2, 4],
    ["t3.large", 2, 8],
]
security_groups = [[]]


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
    author_id = message.author.id

    if cmd == "$생성":
        if args[0] == "eac2":
            pass

    if cmd.isdigit():
        for i in data:
            if data[i]["id"] == author_id:
                if data[i]["qnum"] == 4:
                    data[i]["amount"] = cmd


client.run("token")
