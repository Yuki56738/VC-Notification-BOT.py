#!/usr/bin/python3

import discord
from discord.ext.commands import Bot
from return_token import return_token
import time
import datetime

TOKEN = return_token()
client = discord.Client()

#対象のサーバーの判定フラグ
guild_id = your-guild-id
info_channel = inform-channel-id
flag = 0
time_user_stop = 0000
time_user_start = 0000
dt_now = datetime.datetime.now()
  # datetime.timezone(datetime.timedelta(hours=9))
# )
@client.event
async def on_ready():
    global flag
    global guild_id
    print(f"Logged in as {client.user}")
    print("Connected to following guilds:")
    #for x in client.guilds:
    #    print(f"{x.name}")
    #    if x.id == guild_id:
    #        flag = 1
    #        break
    print(f"debug: time: {dt_now}")
def plusNine(time_str):
  pass
@client.event
async def on_voice_state_update(member, before, after):
    global flag
    global guild_id
    global info_channel
    global time_user_start
    global time_user_stop
    #特定のサーバーでのみ稼働させる
    if member.guild.id == guild_id:
        #入出時
        if before.channel is None:
          print(f"debug: before.channel hitted")
          inf_channel = client.get_channel(info_channel)
          await inf_channel.send(f"{str(datetime.datetime.now())}: {member.name}が{after.channel.name}に入ったよ～")
          # time_user_start = time.time()
          # print(f"{time.time()}")
          
        #退出時
        if after.channel is None:
          print(f"after hitted")
          inf_channel = client.get_channel(info_channel)
        #   await inf_channel.send("after hitted")
          await inf_channel.send(f"{str(datetime.datetime.now())}: {member.name}が{before.channel.name}から出たよ～")
          time_user_stop = time.time()
          # print(f"debug: exit: {int(time_user_stop)-int(time_user_start)}")
    
client.run(TOKEN)
