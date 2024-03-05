import discord
import os
import db as database
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = discord.Bot()

profiles = bot.create_group("profile", "Create/Read/Update/Delete commands for user profile/s")

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    database.setup_database()

@profiles.command(description="Creates a profile to keep track of retrieval!")
async def create(ctx):
    success = database.insert_profile_into_database(ctx.author.id, ctx.author.name)
    if success:
        await ctx.respond(f"Succesfully created a profile for {ctx.author}!")
    else:
        await ctx.respond(f"User profile already exists for {ctx.author} or a database error occured.")


bot.run(DISCORD_TOKEN)