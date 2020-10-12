import os

import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = ".")

gameemojis = ["valorant", "tft", "smash", "skyrim", "rocketleague", "r6", "minecraft", "lol", "forzahorizon", "fallguys", "escapefromtarkov", "dbd", "csgo", "civ6", "amongus"]
gameroles = ["Valorant", "Team Fight Tactics", "Smash Bros Brawl", "Skyrim", "Rocket League", "Rainbow Six Siege", "Minecraft", "League of Legends", "Forza Horizon", 
            "Fall Guys", "Escape from Tarkov", "Dead by Daylight", "CS:GO", "Civilization VI", "Among Us"]

@bot.event
async def on_ready():
    print("started")

@bot.command(name='start', help='start')
async def react(ctx):
    message = await ctx.send("Roles here")
    for emoji in ctx.guild.emojis:
        await message.add_reaction(emoji)

@bot.event
async def on_raw_reaction_add(payload):
    for gameemoji, gamerole in zip(gameemojis, gameroles):
        if payload.emoji.name == gameemoji:
            role = discord.utils.get(guild.roles, name=gamerole)
            if role is not None:
                if payload.member != bot.user:
                    if payload.member is not None:
                        await payload.member.add_roles(role)
                        print("Role: \"{}\" added to {}".format(gamerole, payload.member.name))
                    else:
                        print("Member not found")
            else:
                print("Role not found")

@bot.event
async def on_raw_reaction_remove(payload):
    for gameemoji, gamerole in zip(gameemojis, gameroles):
        if payload.emoji.name == gameemoji:
            role = discord.utils.get(guild.roles, name=gamerole)
            if role is not None:
                if payload.member != bot.user:
                    if payload.member is not None:
                        await payload.member.remove_roles(role)
                        print("Role: \"{}\" added to {}".format(gamerole, payload.member.name))
                    else:
                        print("Member not found")
            else:
                print("Role not found")
  

bot.run(Hier Bot Token platzieren)


