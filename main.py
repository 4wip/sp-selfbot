import discord
from discord.ext import commands
import time
from pypresence import Presence
from open import open

bot = commands.Bot(command_prefix='*', self_bot=True)
rpc = Presence(client_id=)

@bot.event
async def on_ready():
    print('Logged on as', bot.user)

try:
    rpc.connect() 
    rpc.update(
        details="", 
        large_image="", 
        large_text="",
        buttons=[
        {"label": "NOM BOUTON 1", "url": "LIEN 1"},
        {"label": "NOM BOUTON 2", "url": "LIEN 2"}
        ]
    )
except Exception as e:
    print(f"{e}")

@bot.command()
async def ping(ctx):
    await ctx.message.delete()
    await (await ctx.send("...")).edit(content=f"`{round((time.monotonic() - time.monotonic()) * 1000)} ms`")

open()
bot.run('')
