import os

import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = ".")

gameEmojis = ["valorant", "tft", "smash", "skyrim", "rocketleague", "r6", "minecraft", "lol", "forzahorizon", "fallguys", "escapefromtarkov", "dbd", "csgo", "civ6", "amongus", "guest", "uni", "weeb"]
gameRoles = ["Valorant", "Team Fight Tactics", "Smash Bros Brawl", "Skyrim", "Rocket League", "Rainbow Six Siege", "Minecraft", "League of Legends", "Forza Horizon", 
            "Fall Guys", "Escape from Tarkov", "Dead by Daylight", "CS:GO", "Civilization VI", "Among Us", "Guest", "Uni", "Weeb"]

@bot.event
async def on_ready():
    print("started")

@bot.command(name='start', help='start the react message')
async def react(ctx):
    message = await ctx.send("Roles here")
    for emoji in ctx.guild.emojis:
        await message.add_reaction(emoji)
        
@bot.command(name="version", help="get the version")
async def version(ctx):
    await ctx.send("1.2")
    
@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send("Moin, bitte ändere deinen Nicknamen im CGT Discord zu \"Normaler Nickname\" | \"Dein real life Namen\"")
    await member.dm_channel.send("Im Channel \"game-roles\" kannst du dir die jeweiligen Rollen zu den Spielen holen, die du spielst")

@bot.event
async def on_raw_reaction_add(payload):
    guildId = payload.guild_id
    guild = discord.utils.find(lambda g : g.id == guildId, bot.guilds)
    for gameEmoji, gameRole in zip(gameEmojis, gameRoles):
        if payload.emoji.name == gameEmoji:
            role = discord.utils.get(guild.roles, name=gameRole)
            if role is not None:
                if payload.member != bot.user:
                    if payload.member is not None:
                        await payload.member.add_roles(role)
                        print("Role: \"{}\" added to {}".format(gameRole, payload.member.name))
                    else:
                        print("Member not found")
            else:
                print("Role not found")

@bot.event
async def on_raw_reaction_remove(payload):
    guildId = payload.guild_id
    guild = discord.utils.find(lambda g : g.id == guildId, bot.guilds)
    for gameEmoji, gameRole in zip(gameEmojis, gameRoles):
        if payload.emoji.name == gameEmoji:
            role = discord.utils.get(guild.roles, name=gameRole)
            if role is not None:
                if payload.member != bot.user:
                    if payload.member is not None:
                        await payload.member.remove_roles(role)
                        print("Role: \"{}\" added to {}".format(gameRole, payload.member.name))
                    else:
                        print("Member not found")
            else:
                print("Role not found")
  

bot.run("NzY0NDE1NDg1MDc2MTc2OTI3.X4F7ZQ.dC4Hyln3HEUNpB_yYfQmVX29sTg")


