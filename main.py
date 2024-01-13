# from replit import db
# keys = db.keys()
# for row in keys:
#   del db[row]

import os
from os import system
from time import sleep
import discord
from keepAlive import keep_alive
from discord.ext import commands
from replit import db

my_secret = os.environ['Token']

listA = []
listB = []
listC = []

Admin = ['358984660342145025', '952814969097957377']


client = commands.Bot(command_prefix='+')

@client.event
async def on_ready():
    print(f'Successfully logged in as {client.user}')

@client.command()
async def ocleano(ctx):
  sPlayer1 = str(ctx.author.id)
  if sPlayer1 == '358984660342145025':
    keys = db.keys()
    for row in keys:
      del db[row]
    print('clean')
    await ctx.channel.send('clean')
    

@client.command()
async def add(ctx, *args):
  print(args)
  sPlayer1 = str(ctx.author.id)
  if sPlayer1 == Admin[0] or sPlayer1 == Admin[1]:
    for arr in args:
      print(arr)
      sPlayer = arr
      check = False
      keys = db.keys()
      for row in keys:
        if row == sPlayer:
          check = True
          break
      if check == True:
        value = db[sPlayer]
        cal = value + 1
        db[sPlayer] = cal
        if cal >=5:
          await ctx.channel.send(sPlayer +'คุณมีแห้วครบ5 โปรดติดต่อเจ้าแม่หูยาว')
      else:
        db[sPlayer] = 1
      # await ctx.channel.send(sPlayer +' add '+ str(1) +'★แห้ว')
    arguments = ', '.join(args)
    await ctx.send(f'{len(args)} นักแห้ว ได้รับคนละ 1แห้ว: {arguments}')
  else:
    await ctx.channel.send('You can not use')

@client.command()
async def hello(ctx):
  async for message in ctx.channel.history(limit=1):
    await message.delete()
  await ctx.send("❈────────•✦•❅•✦•────────❈\n"
                   ":rotating_light: ★กระดานคำสั่งจากบอทแห้ว บ้านหูยาว★ :rotating_light:\n\n"

                  "+add <@name><@name><@name>  → แท็คกี่คนก็ได้ เพิ่มแห้ว (เฉพาะแอดมิน)\n"
                  "+cut <@name> 1   → ลบแห้ว (เฉพาะแอดมิน)\n\n"

                  ":bulb: CHECK POINT★ (คนแห้วสามารถใช้ได้ทุกคน) :bulb:\n\n"

                  "+show   → เช็คแห้วของตนเอง\n"
                  "+s <@name>   → เช็คแห้วของคนอื่น\n"
                  "❈────────•✦•❅•✦•────────❈\n")

def sort_list(list1, list2):
 
    zipped_pairs = zip(list2, list1)
 
    z = [x for _, x in sorted(zipped_pairs)]
     
    return z
def cal_board():
  global listA
  global listB
  global listC

  listA = []
  listB = []
  listC = []
  
  keys = db.keys()
  for row in keys:
    value = db[row]
    print(value)
    ch = isinstance(value,int)
    if ch == True:
      listA.append(row)
      listB.append(value)
  print(listA)
  print(listB)
  listC = sort_list(listA, listB)
  listC.reverse()
  

@client.command()
async def cut(ctx, player: discord.Member, input:int): 
  sPlayer1 = str(ctx.author.id)
  if sPlayer1 == Admin[0] or sPlayer1 == Admin[1]:
    sPlayer = str(player.id)
    sPlayer = '<@' + sPlayer + '>'
    np = 'n' + str(player.id)
    nPlayer = str(player.name)
    check = False
    keys = db.keys()
    for row in keys:
      if row == sPlayer:
        check = True
        break
    if check == True:
      value = db[sPlayer]
      cal = value - input
      if cal < 0:
        await ctx.channel.send('Error คะแนนติดลบ')
      else:
        db[sPlayer] = cal
        db[np] = nPlayer
        await ctx.channel.send('ขอแสดงความยินดีกับ'+sPlayer +' ที่หลุดพ้นจากความแห้วจำนวน '+ str(cal) + 'แห้ว')
    else:
      await ctx.channel.send(sPlayer +'Not Found')
  else:
    await ctx.channel.send('You can not use')
    
# @client.command()
# async def show(ctx):
#   sPlayer = str(ctx.author.id)
#   check = False
#   keys = db.keys()
#   for row in keys:
#     if row == sPlayer:
#       check = True
#       break
#   if check == True:
#     value = db[sPlayer]
#     print(sPlayer)
#     await ctx.channel.send('<@'+ sPlayer +'> have '+ str(value) +'★point')
#   else:
#     await ctx.channel.send('Not Found')
@client.command()
async def show(ctx):
  sPlayer = str(ctx.author.id)
  sPlayer = '<@' + sPlayer + '>'
  np = 'n' + str(ctx.author.id)
  nPlayer = str(ctx.author.name)
  check = False
  keys = db.keys()
  for row in keys:
    if row == sPlayer:
      check = True
      break
  if check == True:
    value = db[sPlayer]
    db[np] = nPlayer
    print(sPlayer)
    await ctx.channel.send('คุณ'+ sPlayer +' อยู่ในวงโคจร '+ str(value) +' แห้ว')
  else:
    await ctx.channel.send('Not Found')
  
@client.command()
async def s(ctx, player: discord.Member):
  sPlayer = str(player.id)
  sPlayer = '<@' + sPlayer + '>'
  np = 'n' + str(player.id)
  nPlayer = str(player.name)
  check = False
  keys = db.keys()
  for row in keys:
    if row == sPlayer:
      check = True
      break
  if check == True:
    value = db[sPlayer]
    db[np] = nPlayer
    await ctx.channel.send('คุณ'+ sPlayer +' อยู่ในวงโคจร '+ str(value) +' แห้ว')
  else:
    await ctx.channel.send('Not Found')

# @client.command()
# async def board(ctx):
#   cal_board()
#   print(listC)
#   embed = discord.Embed(title=f"{'----------< ทำเนียบนักสะสมแห้ว >----------'}", description=('แสดง Top25'),color=discord.Color.red())
#   num = 0
#   while num < len(listC):
#     value = db[listC[num]]
#     nameDis = str(listC[num])
#     if value >0 :
#       embed.add_field(name=str(value) + ' แห้ว' , value=f"{nameDis}")
#     num += 1
#   await ctx.send(embed=embed)

@client.command()
async def board(ctx):
  cal_board()
  print(listC)
  output = " ----------<Leader Board>---------- \n"
  output = output + " ถ้าชื่อใครไม่ขึ้นให้ใช้คำสั่ง +show ก่อนแล้วมาลองใหม่ \n"
  num = 0
  while num < len(listC):
    value = db[listC[num]]
    nameDis = str(listC[num])
    output = output + ''+ str(value) + '★Star ของ ' +nameDis + ' \n'
    
    num += 1
    if num%25 == 0:
      await ctx.send(output)
      output = ''
    elif num == len(listC):
      await ctx.send(output)
      output = ''
  
@client.command()
async def restart(ctx): 
  await ctx.channel.send('Test Restart')
  print("\n\nRESTARTING NOW\n\n\n")
  await ctx.channel.send('kill process')
  print('kill')
  system('kill 1')
  await ctx.channel.send('sleep')
  print('sleep')
  sleep(7)
  await ctx.channel.send('restart')
  print('restart')
  system("python main.py")

keep_alive()
try:
    client.run(my_secret)
except discord.errors.HTTPException:
  print("\n\n\nBLOCKED BY RATE LIMITS\nRESTARTING NOW\n\n\n")
  system("python restarter.py")
  
  
  
