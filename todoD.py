import os
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = '/')




@bot.event
async def on_ready():
    print("starting...")

@bot.command()
async def 안녕(ctx):
    await ctx.send("안녕!")

@bot.command()
async def 명령어(ctx):
    helpembed=discord.Embed(title="명령어 모음집", description="명령어 모음집", color=0xcca4a4)
    helpembed.add_field(name="일정등록", value="ex) /월요일 발탄12시", inline=True)
    helpembed.add_field(name="요일별 일정보기 ", value="/월요일일정", inline=True)
    helpembed.add_field(name="전체일정보기", value="/전체일정", inline=True)
    helpembed.add_field(name="일정초기화", value="/초기화", inline=False)
    await ctx.send(embed=helpembed)

@bot.command()
async def 월요일(ctx):
    msg = ctx.message.content[4: ]
    await ctx.send(" '[{}]' 월요일 일정에 저장되었습니다. ".format(
        msg))
    file = open('mon.txt', 'w')    # hello.txt 파일을 쓰기 모드(w)로 열기. 파일 객체 반환
    file.write('{}'.format(msg))      # 파일에 문자열 저장
    file.close()
@bot.command()
async def 화요일(ctx):
    msg = ctx.message.content[4: ]
    await ctx.send(" '[{}]' 화요일 일정에 저장되었습니다. ".format(
        msg))
    file = open('tue.txt', 'w')    # hello.txt 파일을 쓰기 모드(w)로 열기. 파일 객체 반환
    file.write('{}'.format(msg))      # 파일에 문자열 저장
    file.close() 
@bot.command()
async def 수요일(ctx):
    msg = ctx.message.content[4: ]
    await ctx.send(" '[{}]' 수요일 일정에 저장되었습니다. ".format(
        msg))
    file = open('wed.txt', 'w')    # hello.txt 파일을 쓰기 모드(w)로 열기. 파일 객체 반환
    file.write('{}'.format(msg))      # 파일에 문자열 저장
    file.close() 
@bot.command()
async def 목요일(ctx):
    msg = ctx.message.content[4: ]
    await ctx.send(" '[{}]' 목요일 일정에 저장되었습니다. ".format(
        msg))
    file = open('thu.txt', 'w')    # hello.txt 파일을 쓰기 모드(w)로 열기. 파일 객체 반환
    file.write('{}'.format(msg))      # 파일에 문자열 저장
    file.close() 
@bot.command()
async def 금요일(ctx):
    msg = ctx.message.content[4: ]
    await ctx.send(" '[{}]' 금요일 일정에 저장되었습니다. ".format(
        msg))
    file = open('fri.txt', 'w')    # hello.txt 파일을 쓰기 모드(w)로 열기. 파일 객체 반환
    file.write('{}'.format(msg))      # 파일에 문자열 저장
    file.close() 
@bot.command()
async def 토요일(ctx):
    msg = ctx.message.content[4: ]
    await ctx.send(" '[{}]' 토요일 일정에 저장되었습니다. ".format(
        msg))
    file = open('sat.txt', 'w')    # hello.txt 파일을 쓰기 모드(w)로 열기. 파일 객체 반환
    file.write('{}'.format(msg))      # 파일에 문자열 저장
    file.close() 
@bot.command()
async def 일요일(ctx):
    msg = ctx.message.content[4: ]
    await ctx.send(" '[{}]' 일요일 일정에 저장되었습니다. ".format(
        msg))
    file = open('sun.txt', 'w')    # hello.txt 파일을 쓰기 모드(w)로 열기. 파일 객체 반환
    file.write('{}'.format(msg))      # 파일에 문자열 저장
    file.close()  


@bot.command()#월요일 일정 보기
async def 월요일일정(ctx):
    file = open('mon.txt', 'r')   
    mo = file.read()

    monembed=discord.Embed(title="요일별 일정 보기", color=0x0080FF)
    monembed.add_field(name="월요일", value="{}".format(mo), inline=False)
    await ctx.send(embed=monembed)
    file.close()

@bot.command()#화요일 일정 보기
async def 화요일일정(ctx):

    file = open('tue.txt', 'r')   
    tu = file.read()

    tueembed=discord.Embed(title="요일별 일정 보기", color=0x01DF01)
    tueembed.add_field(name="화요일", value="{}".format(tu), inline=False)
    await ctx.send(embed=tueembed)
    file.close()

@bot.command()#수요일 일정 보기
async def 수요일일정(ctx):
    file = open('wed.txt', 'r')   
    we = file.read()

    wedembed=discord.Embed(title="요일별 일정 보기", color=0x5F04B4)
    wedembed.add_field(name="수요일", value="{}".format(we), inline=False)
    await ctx.send(embed=wedembed)
    file.close()

@bot.command()#목요일 일정 보기
async def 목요일일정(ctx):
    file = open('thu.txt', 'r')   
    th = file.read()

    thuembed=discord.Embed(title="요일별 일정 보기", color=0xDF01D7)
    thuembed.add_field(name="목요일", value="{}".format(th), inline=False)
    await ctx.send(embed=thuembed)
    file.close()

@bot.command()#금요일 일정 보기
async def 금요일일정(ctx):
    file = open('fri.txt', 'r')   
    fr = file.read()

    friembed=discord.Embed(title="요일별 일정 보기", color=0xFE9A2E)
    friembed.add_field(name="금요일", value="{}".format(fr), inline=False)
    await ctx.send(embed=friembed)
    file.close()

@bot.command()#토요일 일정 보기
async def 토요일일정(ctx):
    file = open('sat.txt', 'r')   
    sa = file.read()

    satembed=discord.Embed(title="요일별 일정 보기", color=0x0000FF)
    satembed.add_field(name="토요일", value="{}".format(sa), inline=False)
    await ctx.send(embed=satembed)
    file.close()

@bot.command()#일요일 일정 보기
async def 일요일일정(ctx):
    file = open('sun.txt', 'r')   
    su = file.read()

    sunembed=discord.Embed(title="요일별 일정 보기", color=0xFF0000)
    sunembed.add_field(name="일요일", value="{}".format(su), inline=False)
    await ctx.send(embed=sunembed)
    file.close()

@bot.command()
async def 전체일정(ctx):
    file = open('mon.txt', 'r')   
    mo = file.read()
    file = open('tue.txt', 'r')   
    tu = file.read()
    file = open('wed.txt', 'r')   
    we = file.read()
    file = open('thu.txt', 'r')   
    th = file.read()                                         
    file = open('fri.txt', 'r')   
    fr = file.read()
    file = open('sat.txt','r')   
    sa = file.read()
    file = open('sun.txt', 'r')   
    su = file.read()

    embed=discord.Embed(title="이번주 일정", color=0x4e9ec1)
    embed.add_field(name="월요일", value="{}".format(mo), inline=False)
    embed.add_field(name="화요일", value="{}".format(tu), inline=False)
    embed.add_field(name="수요일", value="{}".format(we), inline=False)
    embed.add_field(name="목요일", value="{}".format(th), inline=False)
    embed.add_field(name="금요일", value="{}".format(fr), inline=False)
    embed.add_field(name="토요일", value="{}".format(sa), inline=False)
    embed.add_field(name="일요일", value="{}".format(su), inline=False)
    embed.set_footer(text="지원이의 일정")
    await ctx.send(embed=embed)
    file.close()

@bot.command()
async def 전체초기화(ctx):
    await ctx.send('모든 일정을 초기화 할까요?(초기화후 복구 불가능) \n [/네 or /아니오]')
@bot.command()
async def 네(ctx):
    await ctx.send('일정이 초기화 되었습니다.')
    file = open('mon.txt', 'w')    
    file.write('없음')         
    file.close()
    file = open('tue.txt', 'w')    
    file.write('없음')         
    file.close()
    file = open('wed.txt', 'w')    
    file.write('없음')         
    file.close()
    file = open('thu.txt', 'w')    
    file.write('없음')         
    file.close()
    file = open('fri.txt', 'w')    
    file.write('없음')         
    file.close()
    file = open('sat.txt', 'w')    
    file.write('없음')         
    file.close()
    file = open('sun.txt', 'w')    
    file.write('없음')         
    file.close()


@bot.command()
async def 아니오(ctx):
    await ctx.send('일정이 유지됩니다.')

bot.run(os.environ['token'])

