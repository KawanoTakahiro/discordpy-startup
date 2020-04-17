from discord.ext import commands
import os
import traceback
import random
import discord
from discord.ext import tasks
from datetime import datetime

bot = commands.Bot(command_prefix='/')
#client = discord.Client()
token = os.environ['DISCORD_BOT_TOKEN']

@bot.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('パワーーーーーーー！！')

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def power(ctx):
    await ctx.send('パワーーーーーーーーー！！')

async def loop():
    now = datetime.now().strftime('%H:%M')
    if now == '12:00':
        channel = client.get_channel(695294256603988009)
        await channel_send("筋トレだ、ヤーーーーー！！")

bot.run(token)
