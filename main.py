import os
import discord

from discord.ext import commands

TOKEN = os.getenv("DISCORD_TOKEN", None)
LOG_CHANNEL_ID = int(os.getenv("LOG_CHANNEL_ID", 0))

bot = commands.Bot(
    command_prefix="!",
    intents=discord.Intents.all(),
)


@bot.event
async def on_ready():
    print(f"[+] Bot ready. Username: {bot.user}")


@bot.event
async def on_message_delete(message):
    embed = discord.Embed(
        title=f"{message.author.name} deleted a message.",
        description="",
        color=0xff0000,
    )

    embed.add_field(
        name="Message contents",
        value=message.content,
    )

    log_channel = bot.get_channel(LOG_CHANNEL_ID)
    await log_channel.send(embed=embed)


@bot.event
async def on_message_edit(message_before, message_after):
    embed = discord.Embed(
        title=f"{message_before.author.name} edited a message.",
        description="",
        color=0x0000ff,
    )

    embed.add_field(
        name="Before",
        value=message_before.content,
    )

    embed.add_field(
        name="After",
        value=message_after.content,
    )

    log_channel = bot.get_channel(LOG_CHANNEL_ID)
    await log_channel.send(embed=embed)


bot.run(TOKEN)
