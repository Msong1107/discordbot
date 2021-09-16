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

    if message.content.startswith("$생성 ec2"):
       id = message.author.id
        qnum = 1
        instance_name = args[1]
        data["id"] =id
        data["qnum"]=qnum
        data["instance_name"] = instance_name


client.run("token")
