import discord
import os
import db as database
from dotenv import load_dotenv

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = discord.Bot()

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    database.setup_database()


bot.run(DISCORD_TOKEN)