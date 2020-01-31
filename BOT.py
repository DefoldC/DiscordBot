import discord
from discord.ext import commands


client = commands.Bot( command_prefix = '!')

AllowRoles = [
 537678053518737428,
 671863190862430208,
 671864442757185547,
]
EventMessage =[
[671869514354393088,672397783642406912,'❌',671864442757185547],
[671869514354393088,672397783642406912,'✅',671864442757185547],
]

#заготовки
def checkAuthor(x):
    for r in x:
        if r.id in AllowRoles:
            return True
    return False




@client.event

async def on_ready():
    print('BOT connected')

@client.event

async def on_raw_reaction_add(payload):
    for x in EventMessage:
        z=[payload.channel_id, payload.message_id, payload.emoji.name]
        if x[:3]==z[:3]:
            role=discord.utils.get(payload.member.guild.roles, id=x[3])
            await payload.member.add_roles(role)
            return



@client.command( pass_context = True )

async def wr( ctx ,*,arg):
    if not checkAuthor(author.roles): return
    author = ctx.message.author
    await ctx.send(f'{ author.mention } OK')
    await client.get_channel(int(arg.split()[0])).send(arg.split(maxsplit=1)[1])

@client.command( pass_context = True )

async def emoji( ctx ,*,arg):
    author = ctx.message.author
    if not checkAuthor(author.roles): return
    channel = client.get_channel(int(arg.split()[0]))
    msg = await channel.fetch_message(int(arg.split()[1]))
    emoji = arg.split()[2]
    await msg.add_reaction(emoji)
    await ctx.send(f'{ author.mention } OK')


token = os.environ.get('BOT_TOKEN')
client.run(str(token))
