#Discord bot for: Reddit Server

#Import desired packages
import discord
import logging
from discord.ext import commands

#Setup basic logging
logging.basicConfig(level=logging.INFO)

#Setup client (bot) parameters
dev = '<@295267797087420416>'
des = 'A discord bot for Reddit Factorio Server'
prefix = '!'
client = commands.Bot(description=des, command_prefix=commands.when_mentioned_or(prefix))

#Log when the bot is ready
@client.event
async def on_ready():
    print(client.user.name + ' is online!')

#Welcome new users and send them a DM with more information
@client.event
async def on_member_join(member):
    server = member.server
    gRole = discord.utils.get(server.roles, name='Guest')
    outChannel = discord.utils.get(client.get_all_channels(), name='general')
    await client.send_message(outChannel, 'Greetings ' + member.mention + ', welcome to the CLAN_NAME_HERE Discord!')
    await client.add_roles(member, gRole)
#Welcome new users and send them a DM with more information
@client.event
async def on_member_join(member):
    await client.send_message(member, 'Welcome to the Reddit Factorio Discord Server; You have already been assigned the Factory Workers role.' +
                    '\n' + 'When you join the server, you will notice that you are not able to build or break anything. This is a protection we have setup.')
					'\n' + 'To change this, you need to message an Admin or Moderator to get permission to build.')
					'\n\n' + 'My purpose is to provide you with the server status and current IP at your conveinience.')
					'\n\n' + 'Use the ```!status``` command to check server status')
#Sends Server Status
@client.command(pass_context=True)
async def Status(ctx):
    user = ctx.message.author
    channel = ctx.message.channel
    await client.send_message(channel, Hey ' + user.mention + ', Heres the status of the Modded Server Currently: https://multicraft.mcprohosting.com/index.php?r=status/677292.png')

client.run('NDMwMTE4MjA1NTA4Mjg4NTEy.DaL8BQ.ihQNDHhy4RETmRVTwzfJbT3lNF8')
