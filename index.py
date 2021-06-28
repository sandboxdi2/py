from re import A
import discord, asyncio, datetime
import random

from discord import client
from discord import colour
from discord import activity
token = "ODU4NjQ3MTIwNjU4MzAwOTY4.YNhLcg.SUKDVL6F2F-cbHSbmcHaIWowMyo"
client = discord.Client()

@client.event
async def on_ready():
    print("Online")
    game = discord.Game("%모든 명령어")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content == "안녕":
        await message.channel.send("응 안녕")
    if message.content == "아 졸리다":
        await message.channel.send("ㅇㅈ 나도 졸려")
    if message.content == "아니":
        await message.channel.send("힝...")
    if message.content == "뭐함":
        await message.channel.send("밥 먹는중")

    if message.content == "%모든 명령어":
         embed = discord.Embed(colour=discord.Colour.red(), title="여기", description="1.청소. (뒤에 숫자) 2.임베드 3.뽑기 4.운세 5.안녕 6. 아 졸리다 6.아니 7.뭐함 8.10초 타이머 9.1분 타이머 10.5분 타이머 11.10분 타이머 12.내정보")
         await message.channel.send(embed=embed)

    if message.content == "임베드":
         embed = discord.Embed(colour=discord.Colour.red(), title="여기", description="임베드")
         await message.channel.send(embed=embed)

    if message.content.startswith("청소."):
        number = int(message.content.split(" ")[1])
        await message.delete()
        await message.channel.purge(limit=number)
        await message.channel.send(f"{number}개의 메시지를 삭제 했어요!")

    if message.content == "뽑기":
        ran = random.randint(0,1)
        if ran == 0:
            d = "꽝"
        if ran == 1:
            d = "당첨"
        await message.channel.send(d)

    if message.content == "운세":
        ran = random.randint(0,1)
        if ran == 0:
            d = "밖에서 지나가다 똥 밟음"
        if ran == 1:
            d = "엄마 한테 혼남."
        await message.channel.send(d)

    if message.content == "10초 타이머":
        await asyncio.sleep(10)
        await message.channel.send(f"{message.author.mention}, 10초가 지났어요!")

    if message.content == "1분 타이머":
        await asyncio.sleep(60)
        await message.channel.send(f"{message.author.mention}, 1분이 지났어요!")

    if message.content == "5분 타이머":
        await asyncio.sleep(300)
        await message.channel.send(f"{message.author.mention}, 5분이 지났어요!")

    if message.content == "10분 타이머":
        await asyncio.sleep(600)
        await message.channel.send(f"{message.author.mention}, 10분이 지났어요!")

    if message.content.startswith("내정보"):
        date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
        embed = discord.Embed(colour=0x00ff00)
        embed.add_field(name="이름", value=message.author.name, inline=True)
        embed.add_field(name="서버닉네임", value=message.author.display_name, inline=True)
        embed.add_field(name="가입일", value=str(date.year) + "년" + str(date.month) + "월" + str(date.day) + "일", inline=True)
        embed.add_field(name="아이디", value=message.author.id, inline=True)
        embed.set_thumbnail(url=message.author.avatar_url)
        await message.channel.send(embed=embed)


client.run(token)