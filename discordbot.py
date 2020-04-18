import discord
from discord.ext import commands
import os, sys
import traceback
import random
from discord.ext import tasks
from datetime import datetime

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_ready():
    print('パワーーーーーーー！！')

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def power(ctx):
    await ctx.send('パワーーーーーーーーー！！')


@bot.event
async def on_message(message):
    if 'きんにくん' in message.content:
        await message.channel.send('パソコン、Python、パワーーーーーーー！！')

    if "筋トレ" in message.content:
        kaisu = ["10", "15", "20", "25", "30", "35", "40"]
        syurui = ["腕立て", "腹筋", "背筋", "スクワット", "プランク", "全部"]
        choice1 = random.choice(kaisu) #randomモジュール使用
        choice2 = random.choice(syurui) #randomモジュール使用
        unit = "秒" if choice2 == "プランク" else "回"
        await message.channel.send(f"{choice2}を{choice1}{unit}！ヤーー！！")

    if "アーイアアーイ" in message.content:
        await message.channel.send("EVERYBODY PASSION")
        await bot.logout()
        await sys.exit()

@tasks.loop(seconds=60)
async def loop():
    try:
        now = datetime.now().strftime('%H:%M')
        if now == '07:20':
            print("now")
            channel = bot.get_channel(695294256603988009)
            await channel.send('筋トレだ、ヤーーーーー！！')
    except:
        print("エラー")
loop.start()
bot.run(token)
