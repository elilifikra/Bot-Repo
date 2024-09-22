from ayarlar import ayarlar
import discord
from discord.ext import commands
# import * - kütüphanedeki tüm dosyaları içe aktarmanın hızlı bir yoludur
from bot_mantik import *
import random
# ayricaliklar (intents) değişkeni botun ayrıcalıklarını depolayacak
ayricaliklar = discord.Intents.default()
# Mesajları okuma ayrıcalığını etkinleştirelim
ayricaliklar.message_content = True
# istemci (client) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaralım
bot = commands.Bot(command_prefix='+', intents=ayricaliklar)
# Bot hazır olduğunda adını yazdıracak!
@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')
@bot.command()
async def hello(ctx):
    await ctx.send('Selam! Ben bir botum!')
@bot.command()
async def smile(ctx):
    await ctx.send(emoji_olusturucu())
@bot.command()
async def coin(ctx):
    await ctx.send(yazi_tura())
@bot.command()
async def password(ctx, pass_length = 10):
    await ctx.send(sifre_olusturucu(pass_length))

@bot.command()
async def rand_num(ctx, max_num = 10):
    x = rand_number(max_num)
    await ctx.send(x)
bot.run(ayarlar["TOKEN"])