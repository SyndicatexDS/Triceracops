import keep_alive
import discord
import os
import json

from discord.ext import commands

class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot("*", intents = intents)
# bot = commands.when_mentioned_or("*")

# HELP
bot.remove_command("help") # To create a personal help command 

# Load cogs
if __name__ == '__main__':
    for filename in os.listdir("Cogs"):
        if filename.endswith(".py"):
            bot.load_extension(f"Cogs.{filename[:-3]}")

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    print(discord.__version__)
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name =f"{bot.command_prefix}New Survivors that join The Land of Ark"))
keep_alive.keep_alive()
# ------------------------ RUN ------------------------ # 
with open("configuration.json", "r") as config:
    data = json.load(config)
    token = data["token"]
bot.run(token) 