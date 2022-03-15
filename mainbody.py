import discord
import os
from keep_alive import keep_alive
import time

intents = discord.Intents().default()
intents.members = True
client = discord.Client(intents=intents)
saat = time.asctime()


#ödev girdi yapılacak

@client.event
async def on_member_join(member):
  guild = client.get_guild(FILL HERE)
  channel = client.get_channel(FILL HERE)
  await channel.send(f'{member.mention} sınıfa katıldı! Lütfen kullanıcı adını gerçek ismin yap!')
  print('I am ready to engage')


@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_ready():
  await client.change_presence(activity= discord.Game(name='Visual Studio Code')) 

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('Selam'):
    await message.channel.send('Selam!')

  if message.content.startswith('!online'):
    await message.channel.send('https://douonline.dogus.edu.tr/')


  if message.content.startswith('!program'):
    await message.channel.send('https://obs.dogus.edu.tr/oibs/bologna/index.aspx?lang=tr&curOp=showPac&curUnit=3&curSunit=76#')
  
  if message.content.startswith('!okul'):
    await message.channel.send('https://www.dogus.edu.tr/')


  if message.content.startswith('!yapımcılar'):
    await message.channel.send('Bu bot Bilge Kağan Eriş ve Emir Ekrem Kaya tarafından yazıldı!')

  if message.content.startswith('!obs'):
    await message.channel.send(' https://obs.dogus.edu.tr/oibs/ogrenci/login.aspx ')

  if message.content.startswith('!yardım'):
    await message.channel.send('Lütfen yöneticileri etiketleyiniz.')

  if message.content.startswith('selam'):
    await message.channel.send('Selam! ')

  if message.content.startswith('!ehizmet'):
    await message.channel.send('https://www.dogus.edu.tr/e-hizmetler')
  
  if message.content.startswith('!klüpler'):
    await message.channel.send('https://www.dogus.edu.tr/ogrenci/saglik-kultur-ve-spor-hizmetleri-mudurlugu/ogrenci-kulupleri')

  if message.content.startswith('teşekkür ederim'):
    await message.channel.send('Rica Ederiz')

  if message.content.startswith('!share'):
    await message.channel.send('http://dushare.dogus.edu.tr/')

  if message.content.startswith('!bilgislem'):
    await message.channel.send('https://www.dogus.edu.tr/hakkimizda/idari-birimler/bilgi-islem-merkezi')

  

  






keep_alive()
client.run(os.getenv('TOKEN'))
