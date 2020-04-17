from discord.ext import commands
import os
import traceback
import random
from discord.ext import tasks
from datetime import datetime
import discord

bot = commands.Bot(command_prefix='/')
client = discord.Client()
token = os.environ['DISCORD_BOT_TOKEN']

@client.event
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
bot.run(token)

@client.event
async def on_message(message): #メッセージを受け取る関数なので必ず必要
    if message.content == "きんにくん":
        await client.send_message(message.channel, 'パソコン、Python、パワーーーーーーー！！')

    #if message.content == "筋トレ":
       # kaisu = ["10", "15", "20", "25", "30", "35", "40"]
      #  syurui = ["腕立て", "腹筋", "背筋", "スクワット", "プランク", "全部"]
      #  choice1 = random.choice(kaisu) #randomモジュール使用
      #  choice2 = random.choice(syurui) #randomモジュール使用
      #  await message.send_message(message.channel, choice2 "を" choice1 "回！ヤーー！！")
        
@tasks.loop(seconds=60)
async def loop():
    now = datetime.now().strftime('%H:%M')
    if now == '15:00':
        channel = client.get_channel(695294256603988009)
        await channel_send('筋トレだ、ヤーーーーー！！')
loop.start()
client.run("token")
